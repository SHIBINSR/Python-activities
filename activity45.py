               #Bank account

bal=int(input("enter the bank balance:"))
x=int(input("press 1 for credit amount and press 2 for debit amount:"))
if x==1:
    y=int(input("enter the credited amount:"))
    z=bal+y
    print(z)
elif x==2:
    y=int(input("enter the debited amount:"))
    if y<=bal:
        print(bal-y)
    else:
        print("insufficient balance")


