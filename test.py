# """test module to test stuff separetly"""



#making Search account work - not yet

class Bank:
    #note to self: bank account num 5-17 digits; i'll do 5, 0.10% is standard interest or 0.001

    #account search/open account
        #account list
    def __init__(self):
        self.bankName="Oddity Banks"
        self.accountList=[]
        #Account init:(num,holder,interest,bal): rep a bank account

        #hardset accounts
        self.acc1=SavingsAccount(12345,"Percyson Testin",0.001,10000,5000)
        self.acc2=SavingsAccount(54321,"Reed Vers",0.001,300000,5000)
        self.acc3=SavingsAccount(33335,"Ankil Ma",0.001,100,10000)
        self.acc4=ChequingAccount(78910,"Notch E. Bangle",0.002,4000000,6000)
        self.acc5=ChequingAccount(6656, "Quince Ruta",0.002,8080,500)

        #appending to list
        self.accountList.append(self.acc1)
        self.accountList.append(self.acc2)
        self.accountList.append(self.acc3)
        self.accountList.append(self.acc4)
        self.accountList.append(self.acc5)


    def searchAccount(self,accN):
        print(accN,len(self.accountList))  
        for account in self.accountList:
            print(account.getAccountNum(), "is the account num")
            try:
                if (account.getAccountNum()==int(accN)):
                    #returns an actual object
                    return account
            except (TypeError, ValueError):
                pass
        print("This account does not exist")

class Account:
    #note to self: bank account num 5-17 digits; i'll do 5, 0.10% is standard interest or 0.001
    def __init__(self,num,holder,interest,bal): #rep a bank account
        self.accNum=num #int val
        self.accHolderName=holder #string val
        self.rateOfInterest=interest #float val
        self.currentBalance=bal #int val

    def getAccountNum(self):
        return self.accNum
        
    def getAccountHolderName(self):
        return self.getAccountHolderName

    def getRateOfInterest(self):
        return self.rateOfInterest

    def getCurrentBalance(self):
        return self.currentBalance

    #adds deposit to currentBalance
    def deposit(self,dep):
        self.currentBalance+=dep
    
    #removes requested amount if holder has amount and gives it to holder
    def withdraw(self,want):
        if(self.currentBalance-want>=0.01):
            self.currentBalance-=want
            return want
        print("You limit funds to withdraw ${}.".format(self.currentBalance))
        return 0
    
    # #remove afterwards
    # def __str__(self):
    #     a= "hi! I am ",str(self.getAccountHolderName), "with the number",str(self.getAccountNum)
    #     return a


class SavingsAccount(Account):
    def __init__(self,num,holder,interest,bal,mini):
        #child of Account, which restricts withdrawal in account
        super().__init__(num,holder,interest,bal)
        self.minimumBalance=mini

    def withdraw(self,want):
        #note to self: check if this works
        if((self.currentBalance-want)>=self.minimumBalance):
            self.currentBalance-=want
            return want
        #else statement
        print("You limit funds to withdraw ${}.".format(want))
        return 0   


class ChequingAccount(Account):
    pass #child of Account. transactions cannot extend over a given limit
    def __init__(self,num,holder,interest,bal,ovDAllow):
        super().__init__(num,holder,interest,bal)
        self.overdraftAllowed=ovDAllow

    def withdraw(self, want):
        if(want<=self.getCurrentBalance()+self.overdraftAllowed):
            self.currentBalance-=want
            return want
          #else statement
        print("You limit funds to withdraw ${}.".format(want))
        return 0   


stonk=Bank()
print(type(stonk))
print(stonk.searchAccount("myAccount"))
# print(b.searchAccount(12345))

#checking if showAccountMenu works - works
# class Program():
#     def __init__(self):
#         pass
#     def showAccountMenu(self):
#         print("hi")
#     def hi(self):
#         loop=True
#         while loop:
#             try:
#                 selectAcc=int(input("Fantastic. Name the number of the account (5 digit): "))
#                 self.showAccountMenu()
#                 loop=False
#             except ValueError or KeyboardInterrupt:
#                 pass

#checking if withdrawal works - works
# def withdraw(currentBalance,minimumBalance,want):
#     #note to self: check if this works
#     if((currentBalance-want)>=minimumBalance):
#         currentBalance-=want
#         return want
#     print("You limit funds to withdraw ${}.".format(want))
#     return 0

# #current Bal, max takeout, withdrawal
# print(withdraw(7000,5000,1999.99))