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


if __name__ == "__main__":
    w2v_model_path = "../glove50/glove_50_fast.wordvectors"
    model = load_model(w2v_model_path)
    assert model is not None, "Model Loading failed"
    get_word_vector(model,"KING")
