
def ho_add (x) :
    return lambda y: x+y

f = ho_add(10)
print(f(20))
inc = ho_add(1)
print(inc (99))

def ho_add2(x):
    def _add_(y):
        return x+y
    return _add_

f2= ho_add2(10)
print(f2(20))