from vec import Vec

if __name__ == "__main__" :
    v1 = Vec((1,2,3,4,5))

    print(f"Vector 1 : ",v1)

    m = Vec.mean(v1)
    print(f"MEAN : ",m)

    # mv = (m,) * len(v1)
    dmean = Vec.demean(v1)
    print(f"DEMEAN : ",dmean)

    v2 = Vec((10,20,30,40,50))
    std = Vec.std(v2)
    print(f"STANDARD DEVIATION : ",std)