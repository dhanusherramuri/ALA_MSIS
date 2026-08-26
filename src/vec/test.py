from vec import Vec
import sys

if sys.version_info < (3,8):
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
