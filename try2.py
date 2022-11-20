#import business logic and all classes
import BusinessLogic

#attempt 2 on the program because I wrote the program incorrectly

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

                if(user=="O"):
                    print("open")
                    #Bank.openAccount()

                elif(user=="S"):
                    try:
                        acc=int(input(("Fantastic. Please write your account number: ")))
                        if(len(acc)==4):
                            #check if account exists via the method in bank; HERE!!
                            #bank.searchAccount(acc)
                            self.showAccountMenu(acc)

                    except Exception:
                        print("1. There was an error in the input")
                    finally: 
                        print(self.line)
                    

                else:
                    print("Please select a proper option or type EXIT to leave.\n"+self.breakLine)

            except Exception:
                pass
            
            finally:
                print(self.breakLine)

    def showAccountMenu(self,accountNum): #HERE
        print(self.breakLine+"\nWelcome to Account {}. This is the account menu.".format("TEMP-account.getAccNum()"))


    #run code
    def run(self):
        print("Welcome to Oddity Banks!\nHow can I help you?")
        self.showMainMenu()
        print("\nHave a good one, customer!")

#consider making seperate files for better organization?? yes boi


#main code
main=Program()
main.run()
