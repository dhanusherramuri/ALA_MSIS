from builtins import Exception
import os
import math
import re
import numpy as np
import random
from typing import Self
try:
    from gensim.models import KeyedVectors
except ImportError:          # lets the unit tests run on a machine without gensim
    KeyedVectors = None

'''The source of the words in both of the files has been given here 
    [01] SOURCE " https://www.linkedin.com/posts/director-mit-manipal-76295721b_mitmanipal-manipalinstituteoftechnology-activity-7500793278980870144-F45- "
    [02] SOURCE "https://www.linkedin.com/posts/director-mit-manipal-76295721b_mes2026-manipalentrepreneurshipsummit-activity-7431634024386744320-t68P "
'''

# the 20 tags (all single words, so no averaging is needed for T)
TAGS = ["research", "innovation", "education", "university", "students", "faculty", "campus",
        "engineering", "medicine", "technology", "curriculum", "collaboration", "publication",
        "laboratory", "scholarship", "mentorship", "internship", "entrepreneurship",
        "accreditation", "alumni"]

# starter set from the assignment + the function words that showed up in the LinkedIn text
STOPWORDS = {"a", "an", "the", "and", "but", "or", "in", "on", "at", "to", "for",
             "from", "with", "by", "of", "is", "am", "are", "was", "were", "be",
             "i", "you", "he", "she", "it", "we", "they", "this", "that",
             # added by me after looking at the text
             "our", "their", "has", "have", "as", "can", "not", "its", "us", "who",
             "will", "more", "than", "into", "beyond", "through", "over", "across",
             "hashtag"}


class Vec:
    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements = ()
        else:
            # float() so numpy scalars (float32 etc.) are accepted too
            elements = tuple(src)
            for x in elements:
                if isinstance(x, bool) or not isinstance(x, (int, float, np.integer, np.floating)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.elements = tuple(float(x) for x in elements)

    def tlc_pp(txt_path):
        # NOTE: this no longer writes the cleaned text back into the file, it used to
        # overwrite the original which meant the raw text was lost after one run
        with open(txt_path, "r", encoding="utf-8") as f:
            text = f.read()
        before = len(text.split())
        tokens = Vec.preprocess(text)
        print(f"Number of Tokens Before Preprocessing : {before}")
        print(f"Number of Tokens After preprocessing : {len(tokens)}")
        return tokens

    @staticmethod
    def preprocess(text: str) -> list:
        # order from the assignment: lowercase -> punctuation -> split -> stopwords -> length
        text = text.lower()
        # punctuation is turned into a space (not deleted) so "real-world" becomes two
        # words and "hashtag#mitmanipal" doesn't glue into one junk token
        text = re.sub(r"[^\w\s]", " ", text)
        text = text.replace("_", " ")
        tokens = text.split()
        tokens = [w for w in tokens if w not in STOPWORDS]
        tokens = [w for w in tokens if len(w) > 2]
        return tokens

    def __add__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected Vec: {type(t)}")
        if len(self.elements) != len(t):
            raise TypeError(f"Type error - vectors must be of same dimensions")

        return Vec((round(x + y, 5) for x, y in zip(self.elements, t.elements)))


    def __rmul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        
        return Vec((round(x * scalar, 5) for x in self.elements))

    def __imul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")

        # self.elements = [round(val * scalar, 5) for val in self.elements]
        self.elements = tuple(round(val * scalar, 5) for val in self.elements)
        
        return self 

    def __mul__(self, other: Self) -> Self:
        if not isinstance(other, Vec):
            raise TypeError(f"Expected Vec: {type(other)}")

        if len(self) != len(other):
            raise TypeError("Vectors must be of the same dimensions")

        return Vec(round(x * y, 5)for x, y in zip(self.elements, other.elements))


    def __repr__(self) -> str:
        return repr(self.elements)

    def __len__(self) -> int:
        return len(self.elements)

    def __sub__(self, t: Self) -> Self:
        if not (isinstance(t, Vec)):
            raise TypeError(f"Expected Vec : {type(t)}")

        if len(self.elements) != len(t):
            raise TypeError (f"Vectors should be of the same dimensions")
        return Vec(round(x-y,5) for x,y in zip(self.elements,t.elements))
        # raise RuntimeError("vec subtraction unimplemented")

    def __neg__(self) -> Self:
        return Vec(-x for x in self.elements)

    def __radd__(self, other):
        if not isinstance(other, Vec):
            raise TypeError(f"Vector addition with invalid type: {type(other)}")
                
        return Vec((round(x + y, 5) for x, y in zip(self.elements, other.elements)))
        # raise RuntimeError("vec _radd_ unimplemented")

    def __iadd__(self, other):
        if not isinstance(other, Vec):
            raise TypeError(f"Vector addition with invalid type: {type(other)}")
        if len(self) != len(other):
             raise TypeError(f"Not same Dimensions")
        self.elements = tuple(round(x+y,5) for x,y in zip(self.elements, other.elements))
        return self
        # raise RuntimeError("vec _iadd_ unimplemented")

    # return a vector of @n zeroes. precondition: @n > 0
    @staticmethod
    def zeros(n: int) -> Self:
        if not isinstance(n, int):
            raise TypeError(f"Not of the type int")

        if n <= 0:
            raise ValueError(f"Value less than 0")
        else :
            res = (0,) * n
            return Vec((res))
        # raise RuntimeError("zeros unimpleented")

    # return a vector of @n. precondition: @n > 0
    @staticmethod
    def ones(n: int) -> Self:
        if not isinstance(n, int):
                    raise TypeError(f"Not of the type int")
        
        if n <= 0:
                    raise ValueError(f"Value less than 0")
        else :
                    res = (1,) * n
                    return Vec((res))
        # raise RuntimeError("ones unimpleented")

    # return a vector of @n uniformly distributed numbers in [0, 1]. precondition: @n > 0
    @staticmethod
    def uniform(n: int) -> Self:
         if not isinstance(n, int):
                            raise TypeError(f"Not of the type int")
         if n <= 0:
            raise ValueError(f"Value less than 0")

         return Vec(random.uniform(0, 1) for _ in range(n))
        # raise RuntimeError("random unimpleented")

    # Calculates the Euclidean norm (L2 norm) of the vector.
    # sqrt(e[0]^2 + e[1]^2 + e[2]^2 + ... + e[n-1]^2)


    def check (tags : str) -> Self:
         for tag in tags : 
              if tag not in model.key_to_index :
                   raise ValueError(f"Tag not in vocabulary {tag}")
              vector = model[tag]
            #   print(model[tag].shape) Was written to ensure the size of each vector is 50 
            #   print(f"Tag : {tag}")   this was to print the tag which is followed by the vector embeddings 
            #   print(f"Vector : {vector}") which were real numbers
            #   print(Vec.tssw(model,vector))
            #   print(Vec.get_word_vector(model,vector))
            


    # norm and dot are NOT rounded to 5 places anymore, the rounding was adding
    # ~1e-6 of error which would show up in the Vector vs NumPy comparison
    def norm(self) -> float:
        return math.sqrt(sum(x * x for x in self.elements))
        # raise RuntimeError("norm unimpleented")
        # 

    def dot(self, other: Self) -> float:
        if not isinstance(other, Vec):
            raise TypeError(f"Expected Vec: {type(other)}")
        if len(self) != len(other):
            raise TypeError("Vectors must be of the same dimensions")
        return sum(x * y for x, y in zip(self.elements, other.elements))

    def cosine_similarity(self, other: Self) -> float:
        n1 = self.norm()
        n2 = other.norm()
        if n1 == 0 or n2 == 0:
            raise ValueError("Cosine similarity is undefined for a zero vector")
        return self.dot(other) / (n1 * n2)
        
    def load_model(w2v_model_path : str) -> KeyedVectors :
        try:
            fast_model_path = os.path.expanduser(w2v_model_path)
            return KeyedVectors.load(fast_model_path,mmap = 'r')
        except Exception as e:
            print(f"Failed to load model in word2vec format :{e}")
        return None

    def get_word_vector(model, word :str):
        try :
            v = model[word]
            assert len(v) == 50
            return v
        except KeyError:
            print(f"Word '{word}' not in the model Vocaulary.")
        return None

    def similarity(model, word1 : str, word2 : str):
        try :
            score = model.similarity(word1,word2)
            return round(score,7)
        except KeyError as e:
            print(f"One of the words are not in the model vocabulary : {e}")
        return None

    def csr(model, word1 : str, word2 : str):
        vec1 = Vec.get_word_vector(model,word1)
        vec2 = Vec.get_word_vector(model, word2)
        if vec1 is not None and vec2 is not None:
            score = np.dot(vec1,vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
            return round(score,7)
        return None

    def cipr(model, word1 : str, word2 : str):
        vec1 = Vec.get_word_vector(model,word1)
        vec2 = Vec.get_word_vector(model,word2)

        if vec1 is not None and vec2 is not None and len(vec1) == len(vec2) :
            inner_product = 0.0
            for i in range (len(vec1)) :
                inner_product += round(vec1[i] * vec2[i],7)
            return round(inner_product,7)
        return None

    def tsdw(model):
        v1 = Vec.get_word_vector(model,"research")
        v2 = Vec.get_word_vector(model,"innovation")

        assert v1 is not None and v2 is not None, "Word vectors retrieval failed."
        sim = Vec.similarity(model, "research" ,"innovation")
        assert sim is not None, "Similarity Computation Failed."
        raw_sim = Vec.csr(model, "research", "innovation")
        assert abs(sim - raw_sim) < 1e-6, "Computed Similarity Does not match the Model's Similarity"

    def tssw(model):

        v1 = Vec.get_word_vector(model,"research")
        assert v1 is not None, "Word Vector retrieval failed"
        sim = Vec.similarity(model, "research","research")
        assert sim is not None, "Similarity Computation Failed"
        raw_sim = Vec.csr(model,"research","research")
        assert abs(sim - raw_sim) < 1e-6, "Computed Similarity doesnt match the Model similarity."

    def tip(model) :
        v1 = Vec.get_word_vector(model,"internship")
        inner_product = round(np.dot(v1,v1),7)
        comp_inner_prod = Vec.cipr(model,"internship","internship")
        assert abs(inner_product - comp_inner_prod) < 1e-6, "Computed Similarity doesnt match the Model's Similarity"

    def tms(model, word:str) :
        result = model.most_similar(positive = ['internship','research'],negative = ['job'], topn = 1)
        print(result)

    def norm_word(model, word :str) :
        v = model[word]
        sos = 0
        for i in v:
            sos += i**2
        norm = math.sqrt(sos)
        print(round(norm,7))


# ---------------------------------------------------------------------------
# Part D : tag matrix and text matrix
# ---------------------------------------------------------------------------

def build_tag_matrix(model, tags):
    rows = []
    names = []
    for tag in tags:
        words = tag.split()            # "higher education" -> 2 words, "research" -> 1
        for w in words:
            if w not in model.key_to_index:
                # raising on purpose, silently dropping would leave us with 19 tags
                raise ValueError(f"Tag not in vocabulary: {w}")
        vecs = np.array([model[w] for w in words], dtype=np.float64)
        rows.append(vecs.mean(axis=0))     # mean for multi word, same vector for 1 word
        names.append(tag)
    if len(names) != 20:
        raise ValueError(f"Exactly 20 tags are needed, got {len(names)}")
    T = np.vstack(rows)
    return names, T


def build_text_matrix(model, tokens):
    in_vocab_tokens = []
    oov_tokens = []
    for tok in tokens:
        if tok in model.key_to_index:
            in_vocab_tokens.append(tok)     # repeats are kept on purpose
        else:
            oov_tokens.append(tok)
    if len(in_vocab_tokens) == 0:
        raise ValueError("None of the tokens are in the model vocabulary, nothing to compute.")
    W = np.array([model[t] for t in in_vocab_tokens], dtype=np.float64)
    return in_vocab_tokens, oov_tokens, W


# ---------------------------------------------------------------------------
# Part E : similarity with the Vec class (loops)
# ---------------------------------------------------------------------------

def similarity_matrix_vector_class(W, T):
    n = W.shape[0]
    m = T.shape[0]
    S = [[0.0] * m for _ in range(n)]
    # build the Vec objects of T once, they dont change across words
    t_vecs = [Vec(T[j]) for j in range(m)]
    for i in range(n):
        w_vec = Vec(W[i])
        for j in range(m):
            S[i][j] = w_vec.cosine_similarity(t_vecs[j])
    return np.array(S)


# ---------------------------------------------------------------------------
# Part F : similarity with numpy (one matrix multiplication)
# ---------------------------------------------------------------------------

def similarity_matrix_numpy(W, T):
    W_norm = np.linalg.norm(W, axis=1, keepdims=True)
    T_norm = np.linalg.norm(T, axis=1, keepdims=True)
    if np.any(W_norm == 0) or np.any(T_norm == 0):
        raise ValueError("A row with zero norm was found, cosine similarity is undefined")
    W_hat = W / W_norm
    T_hat = T / T_norm
    return W_hat @ T_hat.T


# ---------------------------------------------------------------------------
# Part H : max pooling rank
# ---------------------------------------------------------------------------

def rank_tags(tag_names, S, in_vocab_tokens):
    S = np.asarray(S)
    scores = S.max(axis=0)              # max over words, one value per tag
    best_idx = S.argmax(axis=0)
    order = np.argsort(-scores)         # descending
    return [(tag_names[j], float(scores[j]), in_vocab_tokens[best_idx[j]]) for j in order]


def main(txt_path, w2v_model_path):
    model = Vec.load_model(w2v_model_path)
    assert model is not None, "Model Loading failed"

    with open(txt_path, "r", encoding="utf-8") as f:
        raw = f.read()
    print(f"Words in source file : {len(raw.split())} (limit is 400)")
    print(f"Number of Tokens Before Preprocessing : {len(raw.split())}")
    tokens = Vec.preprocess(raw)
    print(f"Number of Tokens After preprocessing : {len(tokens)}")

    tag_names, T = build_tag_matrix(model, TAGS)
    in_vocab, oov, W = build_text_matrix(model, tokens)
    print(f"In-vocabulary tokens : {len(in_vocab)}")
    print(f"Out-of-vocabulary tokens : {len(oov)}")
    print(f"Distinct OOV tokens : {sorted(set(oov))}")

    print(T.shape)
    print(W.shape)

    S_vector = similarity_matrix_vector_class(W, T)
    S_numpy = similarity_matrix_numpy(W, T)
    print("S shape :", S_numpy.shape)
    print("np.allclose :", np.allclose(S_vector, S_numpy, atol=1e-6))
    print("max abs difference :", np.max(np.abs(S_vector - S_numpy)))

    ranking = rank_tags(tag_names, S_numpy, in_vocab)
    print(f"\n{'Rank':<6}{'Tag':<20}{'Score':<10}{'Best-matching text word':<26}Match type")
    print("-" * 74)
    for r, (tag, score, word) in enumerate(ranking[:8], start=1):
        kind = "identical" if tag == word else "different word"
        print(f"{r:<6}{tag:<20}{score:<10.4f}{word:<26}{kind}")


if __name__ == "__main__":
    txt_path = "./manipal_tags.txt"
    w2v_model_path = "../glove50/glove_50_fast.wordvectors"
    main(txt_path, w2v_model_path)