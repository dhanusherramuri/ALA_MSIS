from vec import Vec
import math

if __name__ == "__main__" :
    v1 = Vec((1,2,3,4,5))

    m = Vec.mean(v1)
    assert m == 3

    dmean = Vec.demean(v1)
    assert abs(dmean.mean() ) < 1e-9

    v2 = Vec((7,7,7,7))
    edm = Vec.demean(v2)
    assert (abs (edm.mean())) < 1e-9 

    v3 = Vec((10,20,30,40,50))
    std1 = Vec.std(v3)
    assert abs(std1 > 0)

    std2 = Vec.std(v2)
    assert abs(std2)< 1e-9

    print(f"ALL ASSERTIONS PASSED")


'''DOCUMENTATION FOR THE CODE
(1) 'm' gets us the mean of the vector v1 
(2) 'dmean' variable stores the demeaned vector and the assert statement makes sure that the 
MEAN OF DEMEANED VECTOR is 0 and 1e - 9 has been used over here because dmean returns the result
in floating point
(3) 'edm' variable refers to equal demean which means when all the elements passed are equal and
the assert is used to check if the value retured is 0 because same values always returns 0
(4) 'std1' is used to check if the standard deviation of the vector consisting of different elements
returns a value which is greater than 0 because distinct elements have a standard deviation greater than 0
(5) 'std2' is used to check the value of the vector 'v2' which has all the same elements so as to check if 
the property which states that the standard deviation will be 0 for the same vector elements satisfies or not.
    '''