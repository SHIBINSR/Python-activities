              #Even Odd Elements

t=int(input("enter the no of test case:"))
for i in range(t):
    a=int(input("how much value you want:"))
    x=[]
    for i in range(a):
        y=int(input("enter the values:"))
        x.append(y)
    odd=0
    even=0
    for i in x:
        if i%2==1:
            odd+=1
        else:
            even+=1

    print(abs(odd-even))

