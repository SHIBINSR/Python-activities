                    #full numeric pyramid

n=int(input("enter the number of rows:"))
for i in range(n):
    for j in range(n-i-1):
        print(0,end="")
    for j in range(i+1):
        print(i+j+1,end="")
    for j in range(i):
        print(2*i-j,end="")
    for j in range(n-i-1):
        print(0,end="")
    print()


