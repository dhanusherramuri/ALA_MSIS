class UpiTx():
    def __init__(self, sender, receiver, amount):

        #create a UUID Instance (python has a inbuilt library)
        self.tx_id = ?
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        pass

class UpiPaymentTx(UpiTx):
    def __init__(self,sender_handle, receiver_handle, amount):
        #pass the responsibility to 'UpiTX'
        pass

class UpiReceiptTx(UpiTx):
    def __init__(self,sender_handle, receiver_handle, amount):
        #pass the responsibility to 'UpiTx'
        pass


class UpiTxResponse : 
    def __init__(self) :
        pass
    
    def perform_payment_tx(sender, receiver, amount):
        tx = UpiPaymentTx(sender, receiver, amount)
        res = tx.pay() #res :UpiTxResponse
        assert res.status == "OK" or res.status == "FAILED"
        