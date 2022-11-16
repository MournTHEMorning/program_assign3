# """test module to test stuff separetly"""

class Program():
    def __init__(self):
        pass
    def showAccountMenu(self):
        print("hi")
    def hi(self):
        loop=True
        while loop:
            try:
                selectAcc=int(input("Fantastic. Name the number of the account (5 digit): "))
                self.showAccountMenu()
                loop=False
            except ValueError or KeyboardInterrupt:
                pass


Program.hi()
# def withdraw(currentBalance,minimumBalance,want):
#     #note to self: check if this works
#     if((currentBalance-want)>=minimumBalance):
#         currentBalance-=want
#         return want
#     print("You limit funds to withdraw ${}.".format(want))
#     return 0

# #current Bal, max takeout, withdrawal
# print(withdraw(7000,5000,1999.99))