from payment import Payment
from datetime import date
class PayPal:
    number = int
    cvv = int
    date = date.today()


    def __init__(self,id, number,cvv, date):
        super.__init__(id)
        self.number=number
        self.cvv=cvv
        self.date=date