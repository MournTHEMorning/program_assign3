

#THE MAIN ANNOYANCE RIGHT NOW -withdrawal HERE!!!
def withdraw(self,requestedAmount):
    self.curBal=0
    self.currentOverdraft=0

    if (requestedAmount>=0 and (requestedAmount>=(self.curBal+self.currentOverdraft) and (self.currentOverdraft<=0 and self.curBal<0))):
        print("Withdraw rejected. Your current balance is ${} CAD, and you have ${} CAD left in your overdraft.".format(self.curBal,self.currentOverdraft))
        return False #False for successful print statement to show or not
    else:
        if(self.curBal<=0):
            self.currentOverdraft-=(requestedAmount)
        self.curBal-=requestedAmount

        print("oui oui oui cheq")
        return True

withdraw(10)