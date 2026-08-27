import numpy as np
import timeit

sizes = [2000, 4000, 8000, 16000, 32000, 64000]

for n in sizes:
    v1 = np.random.uniform(size=n)
    v2 = np.random.uniform(size=n)

    add_time = timeit.timeit(
        lambda: v1 + v2,
        number=100
    )

    sub_time = timeit.timeit(
        lambda: v1 - v2,
        number=100
    )

    mul_time = timeit.timeit(
        lambda: v1 * v2,
        number=100
    )

    norm_time = timeit.timeit(
        lambda: np.linalg.norm(v1),
        number=100
    )

    print(f"\nVector size:  {n}")
    print(f"Addition:       {add_time / 100 * 1000:.4f} ms")
    print(f"Subtraction:    {sub_time / 100 * 1000:.4f} ms")
    print(f"Multiplication: {mul_time / 100 * 1000:.4f} ms")
    print(f"Norm:           {norm_time / 100 * 1000:.4f} ms")
