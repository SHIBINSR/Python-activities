                 #nested if else coding

n=int(input("enter a number:"))
if n>=10 and n<=20:
    m=int(input("enter the another number:"))
    sum= m + n
    print(sum)
    if sum>=100:
        print("that is a large sum!")

else:
    print(-1)



