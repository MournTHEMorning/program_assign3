"""APPLICATION.PY: Main module to run code"""
#prog_assign3, application.py created

#use try and except error stuff. No crashing allowed. 
#if crashing is inevitable, tell user of error and say 'see you'
#negative vals for bank info isn't allowed

#main class, user interaction
class Program:
    def __init__(self):
        self.line="-----*-----"
        self.breakLine="=====* * *====="
        print("initialized! CHANGE LATER")
    def showMainMenu(self):
        loop=True
        while loop:
            print("\nOPTIONS [O] | OPEN ACCOUNT [A] | SELECT ACCOUNT [S] | EXIT [EXIT]")
            user=input("YOU SELECTED: ").upper()
            try:
                if(user=="A"):
                    print("open a new account")        
                elif(user=="S"):
                    print("select account")  
                elif(user=="EXIT"):
                    print("Are you sure you want to EXIT?")  
                    leave=input("\nType YES to confirm or anything else to deny: ").upper()
                    if(leave=="YES"):
                        loop=False
                else:
                    print("Please select a proper option...")

            except ValueError:
                pass
            finally:
                print(self.line)
                    

        #has options openAccount, selectAccount and exit
    #    if openAccount etc..
    def showAccountMenu():
        pass
        #has options checkBalance, Deporsit, withdraw, exitAccount
        #checkBalance, deposit, withdraw, exit
    def run(self):
        #shows main menu, beginning user interaction
        print("Welcome to Oddity Banks!\nHow can I help you?")
        self.showMainMenu()
        print("Have a good one, customer!")


class Account:
    pass #rep a bank account

class SavingsAccount(Account):
    #child of Account, which restricts withdrawal in account
    pass
class ChequingAccount(Account):
    pass #child of Account. transactions cannot extend over a given limit

class Bank():
    #account search/open account
        #account list
    def __init__():
        pass
    #make automatic list of 5 accounts. automatic, random stuff you want
    #i.e. name=Sarah, salery=500mil, job=mafia or something
    def searchAccount(self, accountNum):
        #aka logic for Program class
        self.accountNum=accountNum #temp paramenter
        #return account associated with accountNum
    def openAccount():
        pass#open seasame~

#main code
application=Program()
application.run()