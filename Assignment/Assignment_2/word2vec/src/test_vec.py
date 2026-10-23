import unittest
import numpy as np
from w2v import (Vec, TAGS, build_tag_matrix, build_text_matrix,
                 similarity_matrix_vector_class, similarity_matrix_numpy, rank_tags)


class FakeModel:
    """Tiny stand in for the GloVe KeyedVectors so the tests run quickly and
    dont need the 130MB download. Same interface we use: key_to_index and []."""
    def __init__(self, words, dim=50, seed=0):
        rng = np.random.default_rng(seed)
        self.key_to_index = {w: i for i, w in enumerate(words)}
        self.vecs = rng.normal(size=(len(words), dim)).astype(np.float32)

    def __getitem__(self, w):
        return self.vecs[self.key_to_index[w]]


EXTRA = ["hackathon", "startup", "summit", "learning", "higher"]
MODEL = FakeModel(TAGS + EXTRA)


class TestSemanticTagging(unittest.TestCase):

    def setUp(self):
        self.tokens = ["research", "hackathon", "xyzqq", "startup", "research", "summit"]
        self.tag_names, self.T = build_tag_matrix(MODEL, TAGS)
        self.words, self.oov, self.W = build_text_matrix(MODEL, self.tokens)
        self.S_vec = similarity_matrix_vector_class(self.W, self.T)
        self.S_np = similarity_matrix_numpy(self.W, self.T)

    # 1
    def test_tag_matrix_shape(self):
        self.assertEqual(self.T.shape, (20, 50))

    # 2
    def test_text_matrix_shape(self):
        n = len(self.words)
        self.assertEqual(n, 5)                 # 6 tokens - 1 oov, repeat kept
        self.assertEqual(self.W.shape, (n, 50))

    # 3
    def test_similarity_shape(self):
        self.assertEqual(self.S_np.shape, (len(self.words), 20))
        self.assertEqual(self.S_vec.shape, (len(self.words), 20))

    # 4
    def test_single_pair_matches(self):
        i = self.words.index("hackathon")
        j = self.tag_names.index("innovation")
        direct = Vec(self.W[i]).cosine_similarity(Vec(self.T[j]))
        self.assertAlmostEqual(direct, self.S_np[i, j], places=8)

    # 5
    def test_allclose(self):
        self.assertTrue(np.allclose(self.S_vec, self.S_np, atol=1e-8))

    # 6
    def test_oov_excluded(self):
        self.assertNotIn("xyzqq", self.words)
        self.assertIn("xyzqq", self.oov)
        self.assertEqual(self.W.shape[0], len(self.tokens) - len(self.oov))

    # 7
    def test_oov_tag_raises(self):
        bad = TAGS[:19] + ["notarealwordxx"]
        with self.assertRaises(ValueError):
            build_tag_matrix(MODEL, bad)
        # multi word tag with one bad component should raise too
        bad2 = TAGS[:19] + ["higher notarealwordxx"]
        with self.assertRaises(ValueError):
            build_tag_matrix(MODEL, bad2)

    # extra checks
    def test_multiword_tag_is_mean(self):
        tags = TAGS[:19] + ["higher education"]
        _, T = build_tag_matrix(MODEL, tags)
        expected = (MODEL["higher"].astype(np.float64) + MODEL["education"].astype(np.float64)) / 2
        self.assertTrue(np.allclose(T[19], expected))

    def test_identical_word_gives_one(self):
        i = self.words.index("research")
        j = self.tag_names.index("research")
        self.assertAlmostEqual(self.S_np[i, j], 1.0, places=8)

    def test_no_usable_words_raises(self):
        with self.assertRaises(ValueError):
            build_text_matrix(MODEL, ["xyzqq", "abcdd"])

    def test_rank_tags(self):
        ranking = rank_tags(self.tag_names, self.S_np, self.words)
        scores = [r[1] for r in ranking]
        self.assertEqual(scores, sorted(scores, reverse=True))
        self.assertEqual(ranking[0][0], "research")      # exact match -> score 1
        self.assertEqual(ranking[0][2], "research")

    def test_preprocess(self):
        toks = Vec.preprocess("The Research, at MIT!! #innovation it is ok")
        self.assertEqual(toks, ["research", "mit", "innovation"])


if __name__ == "__main__":
    unittest.main()