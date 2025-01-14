                 #counts the digits

t=int(input("enter the total numbers:"))
while t>0:
    n=int(input("enter the numbers:"))
    count=0
    if n==0:
        count+=1
    while n>=1:
        n/=10
        count+=1
    print(count)
    t-=1
