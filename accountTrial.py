#to test account and if it works

#,rate_of_interest,current_Balance
#account = culminative
class Account:
    def __init__(self,num,holder,savBal,cheqBal):
        self.num=num
        self.holder=holder
        self.roi=0.1
        self.curBal=savBal+cheqBal

        # ChequingAccount(self.num+2,self.holder,0)

    #4 digit number
    def getAccNum(self):
        return self.num

    # one user    
    def getAccHolder(self):
        return self.holder
    def getROI(self):
        return self.roi
    def getCurrentBal(self):
        return self.curBal


    def deposit(self):
        print("deposit :)")
        
    def withdraw(self):
        print("withdrawww")



#class SavingsAccount
class SavingsAccount(Account):
    def __init__(self,num,holder,savBal):
        super().__init__(num,holder,savBal,0)
        self.roi=0.1



#class ChequingAccount
class ChequingAccount(Account):
    def __init__(self):
        pass



#main code
a=Account(1234,"tester1",1000,5000)
print(a.getAccHolder(), a.getAccNum(),a.getCurrentBal(),a.getROI())