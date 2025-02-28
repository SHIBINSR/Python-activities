                 #amstrong numbers

n=int(input("enter the number:"))
a=1
while a<=n:

    temp=a
    z=0
    while temp>=1:
    
        x=int(temp%10)
        y=(x**3)
        z+=y
        
        temp/=10

    if a==z:
        print(a)

    a+=1


