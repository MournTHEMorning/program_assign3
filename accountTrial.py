#to test account and if it works

#,rate_of_interest,current_Balance
#account = culminative
class Account:
    def __init__(self,num,holder,savBal,cheqBal):
        self.num=num
        self.holder=holder
        self.roi=0.1    #culminative rate of interest
        self.curBal=savBal+cheqBal  #Account class: sum of savBal and cheqBal. If savings or chequing account, one will equal zero, respectively

    #4 digit number
    def getAccNum(self):
        return self.num

    # one user    
    def getAccHolder(self):
        return self.holder
    
    #get Rate of interest
    def getROI(self):
        return self.roi

    #get currentBalance. get total if in account class, gets specific class balance of cheq or save
    def getCurrentBal(self):
        return self.curBal


    def deposit(self):
        print("deposit :)")
        
    def withdraw(self):
        print("withdrawww")



#class SavingsAccount
class SavingsAccount(Account):
    def __init__(self,num,holder,savBal):
        super().__init__(num+1,holder,savBal,0)
        self.roi=0.1 #savings roi



#class ChequingAccount
class ChequingAccount(Account):
    def __init__(self,num,holder,cheqBal):
        super().__init__(num+2,holder,0,cheqBal)
        self.roi=0 #cheq roi



#main code, testing
total=float(input("give me your total money: "))
while True:
    savingVal=float(input("how much for saving? Rest of it for cheqing: "))
    if savingVal<total:
        cheqVal=total-savingVal
        break

    else:
        print("not cool.")


a=Account(1234,"tester1",savingVal,cheqVal)
print("Account gen: ",a.getAccHolder(), a.getAccNum(),a.getCurrentBal(),a.getROI())

aSave=SavingsAccount(a.getAccNum(),a.getAccHolder(),savingVal)
print("Saving print",aSave.getAccHolder(),aSave.getAccNum(),aSave.getCurrentBal(),aSave.getROI())

aCheq=ChequingAccount(a.getAccNum(),a.getAccHolder(),cheqVal)
print("Cheq print",aCheq.getAccHolder(),aCheq.getAccNum(),aCheq.getCurrentBal(),aCheq.getROI())