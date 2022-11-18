#attempt 2 on the program because I wrote the program incorrectly

class Program:
    def __init__(self):
        self.line="-----*-----"
        self.breakLine="=====* * *====="
        #self.bank=Bank()        

    def showMainMenu(self):
        user=" "
        while user!="EXIT":
            print("\nOPEN ACCOUNT [O] | SELECT ACCOUNT [S] | EXIT [EXIT]")
            try:
                user=input("YOU SELECTED: ").upper()

                if(user=="O"):
                    print("open")

                elif(user=="S"):
                    print("select account")

                else:
                    print("Please select a proper option or type EXIT to leave.\n"+self.breakLine)

            except Exception:
                pass
            
            finally:
                print(self.breakLine)

    def showAccountMenu(self):
        pass

    #run code
    def run(self):
        print("Welcome to Oddity Banks!\nHow can I help you?")
        self.showMainMenu()
        print("\nHave a good one, customer!")

#consider making seperate files for better organization??

#main code
main=Program()
main.run()