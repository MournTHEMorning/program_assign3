#Class Bank
class Bank:
    bankName="Oddity Bank"
    def __init__(self):
        self.accList=[] #change!!!!
        acc1=Account(1234,"Exa Pullwan",5000,4000)
        acc2=Account(2345,"Anna Tracy",100,50)
        acc3=Account(3456,"Aniok Tara",20,0.05)
        acc4=Account(4567,"Pickolas Cage",20000,3000)
        acc5=Account(5678,"Iwan Kim",3000,900)


#class Account, culminative of user
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