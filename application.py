"""APPLICATION.PY: Main module to run code"""
#prog_assign3, application.py created

#use try and except error stuff. No crashing allowed. 
#if crashing is inevitable, tell user of error and say 'see you'
#negative vals for bank info isn't allowed

#main class, user interaction
class Program:
    def __init__(self):
        print("hey")
    def showMainMenu():
        pass
        #has options openAccount, selectAccount and exit
    #    if openAccount etc..
    def showAccountMenu():
        pass
        #has options checkBalance, Deporsit, withdraw, exitAccount
        #checkBalance, deposit, withdraw, exit
    def run():
        pass#shows main menu

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
Program()