#Class Bank
class Bank:
    bankName="Oddity Bank"
    def __init__(self):
        self.accList=[]
        acc1=Account(1234,"Exa Pullwan",5000,4000)
        acc2=Account(2345,"Anna Tracy",100,50)
        acc3=Account(3456,"Aniok Tara",20,0.05)
        acc4=Account(4567,"Pickolas Cage",20000,3000)
        acc5=Account(5678,"Iwan Kim",3000,900)

        #adding accounts on list
        self.accList.append(acc1)
        self.accList.append(acc2)
        self.accList.append(acc3)
        self.accList.append(acc4)
        self.accList.append(acc5)

        #Savings account list
        self.savAccList=[]
        acc1=SavingsAccount(1234,"Exa Pullwan",5000)
        acc2=SavingsAccount(2345,"Anna Tracy",100)
        acc3=SavingsAccount(3456,"Aniok Tara",20)
        acc4=SavingsAccount(4567,"Pickolas Cage",20000)
        acc5=SavingsAccount(5678,"Iwan Kim",3000)

        #adding savings accounts on list
        self.savAccList.append(acc1)
        self.savAccList.append(acc2)
        self.savAccList.append(acc3)
        self.savAccList.append(acc4)
        self.savAccList.append(acc5)

        #Chequing account list
        self.cheqAccList=[]
        acc1=ChequingAccount(1234,"Exa Pullwan",4000)
        acc2=ChequingAccount(2345,"Anna Tracy",50)
        acc3=ChequingAccount(3456,"Aniok Tara",0.05)
        acc4=ChequingAccount(4567,"Pickolas Cage",3000)
        acc5=ChequingAccount(5678,"Iwan Kim",900)

        #adding chequing accounts on list
        self.cheqAccList.append(acc1)
        self.cheqAccList.append(acc2)
        self.cheqAccList.append(acc3)
        self.cheqAccList.append(acc4)
        self.cheqAccList.append(acc5)

    def searchAccount(self,accountSearch):
        for accounts in self.accList:
            if(accounts.getAccNum() == accountSearch):
                return accounts
        return "Oddity Bank does not have this account number. Please open an account with us."

    #searches the savAccList for the respective account. mainAccount parameter should be the main account's num
    def searchSavAccount(self,mainAccount):
        for accounts in self.savAccList:
            if(accounts.getAccNum() == mainAccount+1):
                return accounts


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


#Testing; DELETE LATER
# for account in Bank().accList:
#     print(account.getAccNum())

# for account in Bank().savAccList:
#     print(account.getAccNum())

# for account in Bank().cheqAccList:
#     print(account.getAccNum())