
def ho_add (x) :
    return lambda y: x+y

f = ho_add(10)
print(f(20))
inc = ho_add(1)
print(inc (99))

def ho_add2(x):
    _bias_ = -2
    def _add_(y):
        return x+y + _bias_
    return _add_

f2= ho_add2(10)
print(f2(20))


a=10
b=10
assert a == b
l1 = [10,20,30]
l2 = [10,20,30]
assert l1 == l2
print(a is b) # 'is' keyword is used to check if the compared values are identical or not while comparing 
              # and that is the reason it doesnt work for list but works only for integers.
print (l1 is l2)

l3 = l1 #l3 is just pointing to l1 which means if a value is changed in l3, then that corresponding value in l1 changes too.

l3[2] = 100
print(l3 == l1)
print (l3 is l1)
print ( l1, "after l3[2] has been changed to 100")


class UpiId :
    def __init__(self, id, bank_id):
        self.id = id
        self.bank_id = bank_id

    def __repr__(self):
        return "upi : {" + self.id + "@"+ self.bank_id + "}"

    def __eq__(self,anony):
        return self.id == anony.id and self.bank_id ==  anony.bank_id

    
edrk_upi_id = UpiId("9876543210", "ybl")
stranger_upi_id = UpiId("9988776655", "axl")
# print(edrk_upi_id)

edrk_upi_id_new = UpiId("9876543210", "ybl")
stranger_upi_id_new = UpiId("9876543210", "ybl")

print(edrk_upi_id_new == stranger_upi_id_new)
print(isinstance(edrk_upi_id_new, UpiId))

# stranger = edrk_upi_id
# print("Stranger : ", stranger)
# print(edrk_upi_id is stranger)

#Assignment - Create a Dictionary of Upi Handle & 'Key' must be a phone number

def create_handle(uid : str, bank_id : str):
    return (uid, bank_id)

def read_id(upi_handle):
    return upi_handle[0]

def read_bank_id(upi_handle):
    return upi_handle[1]

upi_handle = create_handle("8019625339","oksbi")
# uh = ("8019","HDFC")
print("\n"+read_id(upi_handle))
print(read_bank_id(upi_handle))

# assert read_id(uh) == "8019"