import uuid
from datetime import  datetime



class UpiTx():
    def __init__(self, sender, receiver, amount):

        #create a UUID Instance (python has a inbuilt library)
        txnid = str(uuid.uuid4().int)
        txntime = datetime.now().strftime("%y%m%d%H%M")
        utr = txnid[:12]
        self.tx_id = f"T{txntime}{utr}"
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        # pass


class UpiPaymentTx(UpiTx):
    def __init__(self,sender_handle, receiver_handle, amount):
        super().__init__(sender_handle,receiver_handle,amount)
        # pass the responsibility to 'UpiTX'

    def pay(self):
        response = UpiTxResponse()
        response.status = "OK"
        return response
        # pass

class UpiReceiptTx(UpiTx):
    def __init__(self,sender_handle, receiver_handle, amount):
        #pass the responsibility to 'UpiTx'
        super().__init__(sender_handle,receiver_handle,amount)
        # pass


class UpiTxResponse : 
    def __init__(self) :
        self.status = "PENDING"
        # pass
    
    def perform_payment_tx(sender, receiver, amount):
        tx = UpiPaymentTx(sender, receiver, amount)
        res = tx.pay() #res :UpiTxResponse
        assert res.status == "OK" or res.status == "FAILED"
        print(f"[SUCCESS] TxID: {tx.tx_id} | From: {tx.sender} -> To: {tx.receiver} | Amt: ₹{tx.amount}")


# base_tx = UpiTx("4444@oksbi","8251@okhdfc","10000")
# print(f"Base Tx ID: {base_tx.tx_id}")

# UpiTxResponse.perform_payment_tx("4444@oksbi","8251@okhdfc","10000")

transactions_to_run = [
    ("4444@oksbi", "8251@okhdfc", "10000"),
    ("user1@okaxis", "user2@okicici", "500"),
    ("dhanush@okpaytm", "edrk@oksbi", "25000"),
]

# Process every item in the list
print("--- Starting Batch Processing ---")
for s, r, a in transactions_to_run:
    UpiTxResponse.perform_payment_tx(s, r, a)