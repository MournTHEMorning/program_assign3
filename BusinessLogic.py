#Class Bank
class Bank:
    bankName="Oddity Bank"
    def __init__(self):
        self.accList=[1]

#class Account
class Account:
    def __init__(self,num,holder,rate_of_interest,current_Balance):
        self.num=num
        self.holder=holder
        self.roi=rate_of_interest
        self.currBal=current_Balance


#class SavingsAccount
class SavingsAccount(Account):
    def __init__(self):
        super().__init__()


#class ChequingAccount
class ChequingAccount(Account):
    def __init__(self):
        super().__init__()
        