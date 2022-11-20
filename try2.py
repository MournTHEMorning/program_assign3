#import business logic and all classes
import BusinessLogic

class Program:
    bank=BusinessLogic.Bank()
    # account=BusinessLogic.Account()
    # save=BusinessLogic.SavingsAccount()
    # cheque=BusinessLogic.ChequingAccount()

    def __init__(self):
        self.line="-----*-----"
        self.breakLine="=====* * *====="

    def showMainMenu(self):
        user=" "
        while user!="EXIT":
            print("\nOPEN ACCOUNT [O] | SELECT ACCOUNT [S] | EXIT [EXIT]")
            try:
                user=input("YOU SELECTED: ").upper()

                #Main Menu[O]: Open an account with the Bank
                if(user=="O"):
                    print("open")
                    #Bank.openAccount()

                #Main Menu[S]: Select Account, switches to AccountMenu
                elif(user=="S"):
                    try:
                        acc=int(input(("Fantastic. Please write your 4-digit account number: ")))
                        if(acc>=1000 and acc<=9999): #checks if the acc is 4 digits, in an integer way

                            #check if account exists via the method in bank; HERE!!
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

    def showAccountMenu(self,askedAccount): #HERE
        accMenu=" "
        print(self.breakLine+"\nWelcome to Account {}. This is the account menu.".format(askedAccount.getAccNum()))

        while accMenu!="RETURN": 
            print("CHECK BALANCE [B] || DEPOSIT [D] || WITHDRAW [W] || RETURN TO MAIN MENU [RETURN]")
            try:
                accMenu=input("YOU SELECTED: ").upper()

                #Account Menu[B]: Checks Balance of Savings, Chequings and Culminative 
                if(accMenu=="B"):
                    print("Savings({}): ${} CAD\nChequing({}): ${} CAD\n----\nCulminative({}): ${} CAD") #ADD FORMAT LATER!!!
                    input("PRESS ANY KEY TO CONTINUE: ")
                
                #Account Menu[D]: Deposits money in Savings or Chequings
                elif(accMenu=="D"):
                    accountType=input("Deposit to Savings[S] or Chequing[C] account? Any other key to leave: ").upper()
                    if accountType=="S":
                        print("save")
                        self.bank.searchSavAccount(askedAccount.getAccNum())
                        



                #Account Menu[W]: Withdraws money in Savings or Chequings

                #Account Menu: Not an option in Account Menu
                else:
                    if(accMenu!="RETURN"):
                        print("Please select a proper option or type RETURN to go to main menu.\n"+self.breakLine)

            except Exception:
                print("2. There was an error in the input")
            finally:
                print(self.breakLine)

    #run code
    def run(self):
        print("Welcome to Oddity Banks!\nHow can I help you?")
        self.showMainMenu()
        print("\nHave a good one, customer!")

#consider making seperate files for better organization?? yes boi


#main code
main=Program()
main.run()
