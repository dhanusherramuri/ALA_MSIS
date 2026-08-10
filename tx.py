class UpiTx():
    def __init__(self, sender, receiver, amount):

        #create a UUID Instance (python has a inbuilt library)
        self.tx_id = ?
        self.sender = sender
        self.receiver = receiver
        pass

class UpiPaymentTx(UpiTx):
    def __init__(self,sender_handle, receiver_handle, amount):
        #pass the responsibility to 'UpiTX'
        pass

class UpiReceiptTx(UpiTx):
    def __init__(self,sender_handle, receiver_handle, amount):
        pass
        