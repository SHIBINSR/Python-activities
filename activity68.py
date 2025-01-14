                       #first vs last

t=int(input("enter the number of test case:"))

for i in range(t):
    n=int(input("enter the number:"))
    last=int(n%10)

    for j in range(n):
        n//=10
        first=n
        if n<10:
            break

    print(first,last)


         #shortcut
# a=input("enter the number:")
# print(a[0],a[-1])