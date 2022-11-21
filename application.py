"""APPLICATION.PY: Main module to run code"""
#import business logic and all classes
import BusinessLogic

class Program:
    bank=BusinessLogic.Bank()

    def __init__(self):
        self.line="-----*-----"
        self.breakLine="=====* * *====="

    def showMainMenu(self):
        user=" "
        while user!="EXIT":
            print("\nSELECT ACCOUNT [S] | EXIT [EXIT]")
            try:
                user=input("YOU SELECTED: ").upper()

                #Main Menu[S]: Select Account, switches to AccountMenu
                if(user=="S"):
                    try:
                        acc=int(input(("Fantastic! Please write your 4-digit general account number: ")))
                        if(acc>=1000 and acc<=9999): #checks if the acc is 4 digits, in an integer way

                            #check if account exists via the method in bank
                            askedAccount=self.bank.searchAccount(acc)
                            if(type(askedAccount)==str):
                                print(askedAccount)
                            else:
                                self.showAccountMenu(askedAccount)
                                print("\n\nWelcome to the main menu!\n")

                    except Exception:
                        print("1. There was an error in the input")
                    finally: 
                        print(self.line)
                    
                #Main Menu: Not an option on the main menu
                else:
                    print("Please select a proper option or type EXIT to leave.\n"+self.breakLine)

            except Exception:
                pass
            
            finally:
                print(self.breakLine)

    def showAccountMenu(self,askedAccount):
        accMenu=" "
        holderSavAcc=self.bank.searchSavAccount(askedAccount.getAccNum()) #gives program the savings account obj
        holderCheqAcc=self.bank.searchCheqAccount(askedAccount.getAccNum()) #gives program the cheq account obj

        print(self.breakLine+"\nWelcome to Account {}. This is the account menu.".format(askedAccount.getAccNum()))

        while accMenu!="RETURN": 
            print("CHECK BALANCE [B] ||| DEPOSIT [D] ||| WITHDRAW [W] ||| RETURN TO MAIN MENU [RETURN]")
            try:
                accMenu=input("YOU SELECTED: ").upper()

                #Account Menu[B]: Checks Balance of Savings, Chequings and Culminative 
                if(accMenu=="B"):
                    print("Savings(Account #{}): ${} CAD\nChequing(Account #{}): ${} CAD\n----\nCulminative(Account #{}): ${} CAD".format(holderSavAcc.getAccNum(),holderSavAcc.getCurrentBal(),holderCheqAcc.getAccNum(),holderCheqAcc.getCurrentBal(),askedAccount.getAccNum(),askedAccount.getCurrentBal()))
                    input("PRESS ANY KEY TO CONTINUE: ")
                
                #Account Menu[D]: Deposits money in Savings or Chequings
                elif(accMenu=="D"):
                    verify=input("Are you sure you want to deposit? Type YES to continue: ").upper()
                    if (verify=="YES"):
                        accountType=input("Deposit to Savings[S] or Chequing[C] account? ").upper()
                        while (accountType!="S" and accountType!="C"):
                            accountType=input("Deposit to Savings[S] or Chequing[C] account? ").upper()
                        cash=float(input("How much money are you depositing?: "))
                        if (accountType=="S" and cash>=0):
                            holderSavAcc.deposit(cash)
                            input("Your Savings deposit has been processed. PRESS ANY KEY TO CONTINUE:")

                            #updates the main account's cur bal 
                            askedAccount.deposit(cash)
                    

                        elif (accountType=="C" and cash>=0):
                            holderCheqAcc.deposit(cash)
                            input("Your Chequing deposit has been processed. PRESS ANY KEY TO CONTINUE:")
                        
                            #updates the main account's cur bal 
                            askedAccount.deposit(cash)

                #Account Menu[W]: Withdraws money in Savings or Chequings
                elif(accMenu=="W"):
                    verify=input("Are you sure you want to withdraw? Type YES to continue: ").upper()
                    if (verify=="YES"):
                        accountType=input("Withdraw from Savings[S] or Chequing[C] account? ").upper()
                        while (accountType!="S" and accountType!="C"):
                            accountType=input("Withdraw from Savings[S] or Chequing[C] account? ").upper()
                        cash=float(input("How much money are you withdrawing?: "))
                        
                        #SAVINGS ACCOUNT
                        if (accountType=="S" and cash>=0):
                            if(holderSavAcc.withdraw(cash)):
                                input("Your Savings withdrawal has been processed. PRESS ANY KEY TO CONTINUE:")
                                #updates the main account's current balance
                                askedAccount.withdraw(cash)

                        #CHEQUING ACCOUNT
                        elif (accountType=="C" and cash>=0):
                            if(holderCheqAcc.withdraw(cash)):
                                input("Your Chequing withdrawal has been processed. PRESS ANY KEY TO CONTINUE:")
                                #updates the main account's current balance
                                askedAccount.withdraw(cash)

                #Account Menu: Not an option in Account Menu
                else:
                    if(accMenu!="RETURN"):
                        print("Please select a proper option or type RETURN to go to main menu.\n"+self.breakLine)

            except Exception:
                print("2. There was an error in the input")

            #ending for the account menu try block
            finally:
                print(self.breakLine)

    #run():runs code for user interaction and begins program
    def run(self):
        print("Welcome to Oddity Banks!\nHow can I help you?")
        self.showMainMenu()
        print("\nHave a good one, customer!")

#---main code----
main=Program()
main.run()