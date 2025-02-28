                    #days in month

a=int(input("enter the month number:"))
if a%2==1:
    print(31,"days")
elif a==2:
    print(28,"days")
elif a%2==0:
    print(30,"days")