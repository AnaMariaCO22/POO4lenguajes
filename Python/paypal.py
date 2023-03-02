from payment import Payment 
class PayPal:
    email=str

    def __init__(self,id, email):
        super.__init__(id)
        self.email=email