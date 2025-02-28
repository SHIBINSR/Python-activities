              #sum of digits #lucian

t=int(input("enter the total numbers:"))
while t>0:
    n=int(input("enter the number:"))
    sum=0
    while n>=1:
        y=n%10
        sum+=y
        n/=10
    print(int(sum))
    t-=1
