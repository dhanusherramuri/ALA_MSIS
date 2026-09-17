from builtins import Exception
import os
import math
import numpy as np
from gensim.models import KeyedVectors


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
    vec1 = get_word_vector(model,word1)
    vec2 = get_word_vector(model, word2)
    if vec1 is not None and vec2 is not None:
        score = np.dot(vec1,vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
        return round(score,7)
    return None

def cipr(model, word1 : str, word2 : str):
    vec1 = get_word_vector(model,word1)
    vec2 = get_word_vector(model,word2)

    if vec1 is not None and vec2 is not None and len(vec1) == len(vec2) :
        inner_product = 0.0
        for i in range (len(vec1)) :
            inner_product += round(vec1[i] * vec2[i],7)
        return round(inner_product,7)
    return None

def tsdw(model):
    v1 = get_word_vector(model,"research")
    v2 = get_word_vector(model,"internship")

    assert v1 is not None and v2 is not None, "Word vectors retrieval failed."
    sim = similarity(model, "research" ,"internship")
    assert sim is not None, "Similarity Computation Failed."
    raw_sim = csr(model, "research", "internship")
    assert abs(sim - raw_sim) < 1e-6, "Computed Similarity Does not match the Model's Similarity"

def tssw(model):

    v1 = get_word_vector(model,"research")
    assert v1 is not None, "Word Vector retrieval failed"
    sim = similarity(model, "research","research")
    assert sim is not None, "Similarity Computation Failed"
    raw_sim = csr(model,"research","research")
    assert abs(sim - raw_sim) < 1e-6, "Computed Similarity doesnt match the Model similarity."

def tip(model) :
    v1 = get_word_vector(model,"internship")
    inner_product = round(np.dot(v1,v1),7)
    comp_inner_prod = cipr(model,"internship","internship")
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

if __name__ == "__main__":
    w2v_model_path = "../glove50/glove_50_fast.wordvectors"
    model = load_model(w2v_model_path)
    assert model is not None, "Model Loading failed"
    tsdw(model)
    tssw(model)
    tip(model)
    tms(model, "internship")
    norm_word(model,"tech")
