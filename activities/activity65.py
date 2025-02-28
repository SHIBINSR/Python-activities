              #first vs last

t=int(input("enter the test cases:"))

while t>0:
    n=int(input("enter the number:"))
    temp=n
    last=n%10
    while temp>0:
        first=int(temp%10)
        temp/=10
    print(first,last)

    t-=1