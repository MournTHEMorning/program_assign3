def withdraw(requestedAmount):

    #temp val
    curBal=5000.5
    currentOverdraft=500

    # if(requestedAmount<0 or (requestedAmount>currentOverdraft)):
    if((curBal<=0 and currentOverdraft<(requestedAmount)) or requestedAmount<0):

        print("Withdraw rejected. Your current balance is ${} CAD, and you have ${} CAD left in your currentOverdraft.".format(curBal,currentOverdraft))
        print("currentOverdraft {} | bal {} | request {}".format(currentOverdraft,curBal,requestedAmount))

        return False #False for successful print statement to show or not
    
    else:
        if(curBal>0):
            curBal-=requestedAmount
            if(curBal<=0):
                currentOverdraft-=abs(curBal)
        #if curBal is less than or greater than zero
        else:
            curBal-=requestedAmount
            currentOverdraft-=requestedAmount

        print("oui oui oui cheq")
        print("currentOverdraft {} | bal {} | request {}".format(currentOverdraft,curBal,requestedAmount))

        return True

withdraw(5100.5)