"""BUSINESSLOGIC.PY: Module that has all classes and methods related to the logic (Classes: Bank, Account, SavingsAccount,ChequingAccount) """
#Class Bank: represents Oddity Bank
class Bank:
    bankName="Oddity Bank"
    def __init__(self):
        #general account list
        self.accList=[]
        #Account(number,holder,savingsBal,chequeBal)
        acc1=Account(1234,"Exa Pullwan",5000.0,4000.0) #acc1, acc2, etc. are temporary and reused to create the respective obj
        acc2=Account(2345,"Anna Tracy",100.0,50.0)
        acc3=Account(3456,"Aniok Tara",20.0,0.05)
        acc4=Account(4567,"Pickolas Cage",20000.0,3000.0)
        acc5=Account(5678,"Iwan Kim",3000.0,900.0)

        #adding accounts on list
        self.accList.append(acc1)
        self.accList.append(acc2)
        self.accList.append(acc3)
        self.accList.append(acc4)
        self.accList.append(acc5)

        #Savings account list
        self.savAccList=[]
        #SavingsAccount(general Account number,holder,savingsBal,minimumBal)
        acc1=SavingsAccount(1234,"Exa Pullwan",5000.0,5000.0)
        acc2=SavingsAccount(2345,"Anna Tracy",100.0,100.0)
        acc3=SavingsAccount(3456,"Aniok Tara",20.0,5.0)
        acc4=SavingsAccount(4567,"Pickolas Cage",20000.0,5000.0)
        acc5=SavingsAccount(5678,"Iwan Kim",3000.0,1000.0)

        #adding savings accounts on list
        self.savAccList.append(acc1)
        self.savAccList.append(acc2)
        self.savAccList.append(acc3)
        self.savAccList.append(acc4)
        self.savAccList.append(acc5)

        #Chequing account list
        self.cheqAccList=[]
        #SavingsAccount(general Account number,holder,chequingBal,overdraft Allowed)
        acc1=ChequingAccount(1234,"Exa Pullwan",4000.0,500.0)
        acc2=ChequingAccount(2345,"Anna Tracy",50.0,1000.0)
        acc3=ChequingAccount(3456,"Aniok Tara",0.05,5000.0)
        acc4=ChequingAccount(4567,"Pickolas Cage",3000.0,10000.0)
        acc5=ChequingAccount(5678,"Iwan Kim",900.0,50.0)

        #adding chequing accounts on list
        self.cheqAccList.append(acc1)
        self.cheqAccList.append(acc2)
        self.cheqAccList.append(acc3)
        self.cheqAccList.append(acc4)
        self.cheqAccList.append(acc5)

    #searchAccount(): looks for account in general list
    def searchAccount(self,accountSearch):
        for accounts in self.accList:
            if(accounts.getAccNum() == accountSearch):
                return accounts
        return "Oddity Bank does not have this account number. Please leave and go to a different bank."

    #searchSavAccount(): searches the savAccList for the respective account. mainAccount parameter should be the main account's num
    def searchSavAccount(self,mainAccount):
        for accounts in self.savAccList:
            if(accounts.getAccNum() == mainAccount+1):
                return accounts

    #searchCheqAccount(): searches the cheqAccList for the respective account. mainAccount parameter should be the main account's num
    def searchCheqAccount(self,mainAccount):
        for accounts in self.cheqAccList:
            if(accounts.getAccNum() == mainAccount+2):
                return accounts


#class Account: culminative of user and parent of SavingsAccount and ChequingAccount
class Account:
    def __init__(self,num,holder,savBal,cheqBal):
        self.num=num
        self.holder=holder
        self.roi=0.1    #culminative rate of interest
        self.curBal=savBal+cheqBal  #Account class: sum of savBal and cheqBal. 
                                        #Children Classes: savBal or cheqBal will equal zero depending if it is savings or chequing account

    #getAccNum(): returns the 4 digit account number
    def getAccNum(self):
        return self.num

    #getAccHolder(): returns the holder of the account    
    def getAccHolder(self):
        return self.holder
    
    #getROI(): returns Rate of interest
    def getROI(self):
        return self.roi

    #getCurrentBal():return currentBalance. It will get the total if in account class, but will get specific balance for children classes
    def getCurrentBal(self):
        return self.curBal

    #deposit(): deposits cash into the current Balance of the account
    def deposit(self,cash):
        self.curBal+=cash
        
    #withdraw(): withdraws cash into the current Balance of the account. Is used by Account class and should not be used by the children classes
    def withdraw(self,cash):
        self.curBal-=cash


#class SavingsAccount: child of Account and is Savings Account
class SavingsAccount(Account):
    def __init__(self,num,holder,savBal,minimum):
        super().__init__(num+1,holder,savBal,0) #see Account class
        self.roi=0.1 #savings roi
        self.minimumBalance=minimum

    #getMiniBal(): returns the minimumBalance
    def getMiniBal(self):
        return self.minimumBalance

    #withdraw(): withdraws from savings account with minimum balance in mind
    def withdraw(self,requestedAmount):
        if (requestedAmount>(self.curBal-self.minimumBalance) and requestedAmount>=0):
            print("Withdraw rejected. Your current balance is ${} CAD, and your minimum balance required in this savings account is ${} CAD.".format(self.curBal,self.minimumBalance))
            return False #False for successful print statement to show or not
        else:
            self.curBal-=requestedAmount
            return True #True for successful print statement to show and changes the culminative current balance respectively


#class ChequingAccount:child of Account and is Chequing Account
class ChequingAccount(Account):
    def __init__(self,num,holder,cheqBal,overdraft):
        super().__init__(num+2,holder,0,cheqBal) #see Account class
        self.roi=0.0 #cheque roi
        self.overdraftAllowed=overdraft
        self.currentOverdraft=overdraft

    #getOverdraftAllowed(): returns overdraftAllowed
    def getOverdraftAllowed(self):
        return self.overdraftAllowed

    #getOverdraft(): returns current overdraft
    def getOverdraft(self):
        return self.currentOverdraft

    #deposit(): different from deposit in Account class, as this includes the possible overdraft debt
    def deposit(self,cash):
        #if the overdraft was used. it must be paid back first.
        if(self.overdraftAllowed!=self.currentOverdraft):
            diff=self.overdraftAllowed-self.currentOverdraft
            if (diff<cash):
                self.currentOverdraft+=diff

            elif (diff>=cash):
                self.currentOverdraft+=cash
       
       #curBal represents both debt from overdraft AND the current positive balance in chequing overall
        self.curBal+=cash

    #withdraw(): withdraws from chequing account
    def withdraw(self,requestedAmount):

        #if requestedAmount cannot be withdrawn
        if((self.curBal<=0 and self.currentOverdraft<(requestedAmount)) or requestedAmount<0):
            print("Withdraw rejected. Your current balance is ${} CAD, and you have ${} CAD left in your self.currentOverdraft.".format(self.curBal,self.currentOverdraft))
            print("self.currentOverdraft {} | bal {} | request {}".format(self.currentOverdraft,self.curBal,requestedAmount))

            return False #False for successful print statement in application.py to show or not

        #if requestedAmount CAN be withdrawn
        else:
            if(self.curBal>0):
                self.curBal-=requestedAmount
                if(self.curBal<=0):
                    self.currentOverdraft-=abs(self.curBal)

            #if self.curBal is less than or greater than zero
            else:
                self.curBal-=requestedAmount
                self.currentOverdraft-=requestedAmount

            return True #True for successful print statement in application.py to show or not