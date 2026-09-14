from vec import Vec
import math

if __name__ == "__main__" :
    v1 = Vec((1,2,3,4,5))

    # print(f"Vector 1 : ",v1)

    m = Vec.mean(v1)
    # print(f"MEAN : ",m)

    # mv = (m,) * len(v1)
    dmean = Vec.demean(v1)
    # print(f"\nDEMEAN OF VECTOR V1: ",dmean)
    # print (f"\nMEAN OF DEMEAN VECTOR V1 : ",Vec.mean(dmean))
    assert abs(dmean.mean() ) < 1e-9

    v2 = Vec((7,7,7,7))
    edm = Vec.demean(v2)
    # print(f"\nDEMEAN OF VECTOR V2: ",edm)
    # print (f"MEAN OF DEMEAN VECTOR V2 : ",Vec.mean(edm))
    assert (abs (edm.mean())) < 1e-9 

    v3 = Vec((10,20,30,40,50))
    std1 = Vec.std(v3)
    # print(f"\nSTANDARD DEVIATION : ",std)
    assert abs(std1 > 0)

    std2 = Vec.std(v2)
    # print(f"\nSTANDARD DEVIATION OF V2 : ",std)
    assert abs(std2)< 1e-9

    print(f"ALL ASSERTIONS PASSED")
    # v4 = Vec(())