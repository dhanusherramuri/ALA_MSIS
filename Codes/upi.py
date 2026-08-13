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

def compare_handles(s,t):
    return s[0] == t[0] and s[1] == t[1]

def test_compare_handles():
    h1 = create_handle("80196","oksbi")
    h2 = create_handle("99896","oksbi")
    
    assert not compare_handles(h1,h2)
    assert  compare_handles(h1,h1)
    assert  compare_handles(h2,h1)

# test_compare_handles()

