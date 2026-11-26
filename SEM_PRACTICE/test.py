import numpy as np

def subvec(self,i,j):
    return self[i-1:j]

x = np.array([1,4,9,16,25,36])

n = len(x)

D = np.zeros((n,n-1),dtype=int)

for i in range(n):
    if i < n-1:
        D[i,i] = -1
    if i > 0:
        D[i,i-1] = 1

result = x.T @ D
print(x[5])
d=x[1:6]-x[0:5]
print(d)
res2 = D.T @ x

np.array_equal(res2,d)


print(subvec(x,2,5))
print(result)


#Question 2
x = np.random.default_rng(0).standard_normal((6,768))

res3 = D.T @ x
print(res3.shape)

#Question 3

def layer_norm(e,gamma,beta,eps=1e-5):
    mean = np.mean(e)
    var  = np.var(e)

    e_hat=np.dot((e-mean)/(np.sqrt(var+eps)),gamma)
    return e_hat+beta

e = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
gamma = 1.0
beta = 0.0

print(layer_norm(e,gamma,beta))