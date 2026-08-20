
import sys
import random
import math
from typing import Self


"""
A custom vector class implementation for educational purposes.
"""

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

        if n < 0:
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
        
        if n < 0:
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
         if n < 0:
            raise ValueError(f"Value less than 0")

         return Vec(random.uniform(0, 1) for _ in range(n))
        # raise RuntimeError("random unimpleented")

    # Calculates the Euclidean norm (L2 norm) of the vector.
    # sqrt(e[0]^2 + e[1]^2 + e[2]^2 + ... + e[n-1]^2)
    def norm(self) -> float:
        return round(math.sqrt(sum(x * x for x in self.elements)), 5)
        # raise RuntimeError("norm unimpleented")


"""
(1) Understand the basic design of the vector abstraction. Review the implementation.
(2) Document each function.
(3) Implement all unimplemented methods.
(4) Create appropriate tests for this implementation, increasing the confidence about its correctness.

(5) Test this implementation by importing the class in a sepatate python script.

(6) Measure the performance of each of these functions on vectors of varying lengths.
    Try 2k to 64k dimension vectors and time the results.
    How would you do the measurements?
    ******** COMPLETED TILL THIS POINT and the time has been used using the timeit function and the time that came has been divided by 10^6 so as to convert it into milliseconds***************

(7) Measure the performance on your machine. Check it on colab.

(8) use numpy and compare the performance.
"""


if sys.version_info < (3, 8):
    sys.exit("Error: This script requires Python 3.8 or higher.")

if __name__ == "__main__":
    #z1 = Vec.zeros(10)
    # v1 = Vec((0, 1, 1.03))
    v1 = Vec((0,1,2.03,-1.04))
    print(v1)
    v3 = 2.2 * v1
    print("2.2 * 1 :",v3)
    ves1 = Vec((1,1,1,1))
    v3 = v3+ves1
    print(f"V3 after adding 1 using add method : ",v3)
    v3 = 5 * v3
    print(f"Vector Multiplication using rmul :",v3)
    # v3 *=  5
    # print(v3)
    # v3 = 1 + v3
    # print(v3)
    v2 = v1+v3
    print(f"Vector addition using Add function : ",v2)

    print(f"v3 : ",v3,"\nV2 :",v2)
    v4 = v3 - v2
    print(f"Vector Subtraction using sub : ",v4)
    v3 *= 5
    print(v3)

    v4 += v3

    print(v4)

    print(Vec.zeros(5))
    print(Vec.ones(5))
    print(Vec.uniform(5))
    print(v4.norm())
    # v_test = Vec((5,6))
    # v5 = Vec.__imul__(v4,1)
    # print(v5)
    # print(v1 + v3)
    #print(-(v1 + v3))
