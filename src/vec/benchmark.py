from vec import Vec
import timeit

sizes = [2000, 4000 , 8000 , 16000 , 32000 , 64000]

for n in sizes :
    v1 = Vec.uniform(n)
    v2 = Vec.uniform(n)

    add_time = timeit.timeit(
        lambda : v1 + v2,
        number= 100
    )

    sub_time = timeit.timeit(
        lambda : v1 - v2,
        number = 100
    )

    mul_time = timeit.timeit(
        lambda : v1 * v2,
        number = 100
    )

    norm_time = timeit.timeit(
        lambda : v1.norm(),
        number = 100
    )


    print(f"\nVector size:  {n}")
    print(f"Addition:       {add_time / 100 * 1000:.4f} ms")
    print(f"Subtraction:    {sub_time / 100 * 1000:.4f} ms")
    print(f"Multiplication: {mul_time / 100 * 1000:.4f} ms")
    print(f"Norm:           {norm_time / 100 * 1000:.4f} ms")
