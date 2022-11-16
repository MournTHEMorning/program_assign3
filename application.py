"""APPLICATION.PY: Main module to run code"""

#use try and except error stuff. No crashing allowed. 
#if crashing is inevitable, tell user of error and say 'see you'
#negative vals for bank info isn't allowed


class Program:  #main class, user interaction
    def __init__(self):
        self.line="-----*-----"
        self.breakLine="=====* * *====="

    def showAccountMenu(self):
        #checks if a valid account
        pass


        #checkBalance, deposit, withdraw, exit

    def showMainMenu(self):
        loop=True;leave=" "
        while loop:
            print("\nOPEN ACCOUNT [O] | SELECT ACCOUNT [S] | EXIT [EXIT]")
            user=input("YOU SELECTED: ").upper()
            try:
                if(user=="O"):
                    print("open a new account")        
                elif(user=="S"):
                    while loop:
                        try:
                            selectAcc=int(input("Fantastic. Name the number of the account (5 digit): "))
                            self.showAccountMenu()
                            loop=False
                        except (ValueError, KeyboardInterrupt):
                            pass
                elif(user=="EXIT"):
                    print("Are you sure you want to EXIT?")  
                    leave=input("\nType YES to confirm or anything else to deny: ").upper()
                    if(leave=="YES"):
                        loop=False
                else:
                    print("Please select a proper option...")

            except (ValueError,EOFError,KeyboardInterrupt):
                print("hey?")

            finally:
                print(self.line)
                if (user!="EXIT" and leave!="YES"):
                    loop=True
                    leave=" "

    def run(self):
        #shows main menu, beginning user interaction
        print("Welcome to Oddity Banks!\nHow can I help you?")
        self.showMainMenu()
        print("Have a good one, customer!")

class Bank: #account search/open account
    #note to self: bank account num 5-17 digits; i'll do 5, 0.10% is standard interest or 0.001
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
            try:
                if (account.getAccountNum()==int(accN)):
                    
                    #returns an actual object associated with the account number
                    return account
            except (TypeError, ValueError):
                pass
        print("This account does not exist")
        
    #method to make an account
    def openAccount():
        pass#open seasame~

class Account: #rep a bank account
    #note to self: bank account num 5-17 digits; i'll do 5, 0.10% is standard interest or 0.001
    def __init__(self,num,holder,interest,bal): 
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
        if(self.currentBalance-want>=0.01 and want>=0.01):
            self.currentBalance-=want
            return want
        print("You limit funds to withdraw ${}.".format(self.currentBalance))
        return 0
    
class SavingsAccount(Account):  #child of Account, which restricts withdrawal in account

    def __init__(self,num,holder,interest,bal,mini):
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

class ChequingAccount(Account): #child of Account. transactions cannot extend over a given limit
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


#main code
application=Program()
application.run()