import numpy as np

a = np.array([1,2,3])

print(a.shape)
print(a.ndim)


print(isinstance(a.shape, tuple))

a = np.zeros(4)
assert(a.all() == 0)
assert(a.any() ==  0)