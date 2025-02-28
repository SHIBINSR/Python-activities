                   #bank account-2

bal=int(input("enter the bank balance:"))
while bal>0:
    op=int(input("press 1 for credit amount,\npress 2 for debit amount and press 3 for exit:"))
    if op==1:
        am=int(input("enter the amount for credit:"))
        bal+=am
        print("balance=",bal)
    elif op==2:
        am=int(input("enter the amount for debit:"))
        if am>bal:
            print("balance=",bal)
            print("insufficient fund")
        else:
            bal-=am
            print("balance=", bal)
    elif op==3:
        print("thanks")
        break
    else:
        print("fool wrong number")

