#THE MAIN ANNOYANCE RIGHT NOW -withdrawal HERE!!!
def withdraw(requestedAmount):
    curBal=-10
    overdraft=0

    # if (requestedAmount>=0 and (requestedAmount>=(curBal+overdraft) and (overdraft<=0 and curBal<0))):
    if(requestedAmount<0 or (requestedAmount>overdraft)):
        print("Withdraw rejected. Your current balance is ${} CAD, and you have ${} CAD left in your overdraft.".format(curBal,overdraft))
        print("overdraft {} | bal {} | request {}".format(overdraft,curBal,requestedAmount))

        return False #False for successful print statement to show or not
    
    else:
        if(curBal>0):
            curBal-=requestedAmount
            if(curBal<=0):
                overdraft-=abs(curBal)
        #if curBal is less than or greater than zero
        else:
            curBal-=requestedAmount
            overdraft-=requestedAmount

        print("oui oui oui cheq")
        print("overdraft {} | bal {} | request {}".format(overdraft,curBal,requestedAmount))

        return True

withdraw(10)