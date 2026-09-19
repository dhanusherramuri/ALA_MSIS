from builtins import Exception
import os
import math
import numpy as np
import random
from typing import Self
from gensim.models import KeyedVectors


class Vec:
    def __init__(self, src=None) -> Self:
        if src is None:
            self.elements = ()
        else:
            elements = tuple(src)
            for x in elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.elements = elements

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
    def norm(self) -> float:
        return round(math.sqrt(sum(x * x for x in self.elements)), 5)
        # raise RuntimeError("norm unimpleented")
        # 
        
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
        v2 = Vec.get_word_vector(model,"internship")

        assert v1 is not None and v2 is not None, "Word vectors retrieval failed."
        sim = Vec.similarity(model, "research" ,"internship")
        assert sim is not None, "Similarity Computation Failed."
        raw_sim = Vec.csr(model, "research", "internship")
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

if __name__ == "__main__":
    w2v_model_path = "../glove50/glove_50_fast.wordvectors"
    model = Vec.load_model(w2v_model_path)
    assert model is not None, "Model Loading failed"
    Vec.tsdw(model)
    Vec.tssw(model)
    Vec.tip(model)
    Vec.tms(model, "internship")
    Vec.norm_word(model,"tech")
