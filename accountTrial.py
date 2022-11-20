#to test account and if it works

class Account:
    def __init__(self,num,holder,rate_of_interest,current_Balance):
        self.num=num
        self.holder=holder
        self.roi=rate_of_interest
        self.currBal=current_Balance

    def getAccNum(self):
        return self.num
    def getAccHolder(self):
        return self.holder
    def getROI(self):
        return self.roi
    def getCurrentBal(self):
        return self.currBal


    def deposit(self):
        print("deposit :)")
        
    def withdraw(self):
        print("withdrawww")



#class SavingsAccount
class SavingsAccount(Account):
    def __init__(self):
        super().__init__()


#class ChequingAccount
class ChequingAccount(Account):
    def __init__(self):
        super().__init__()
        