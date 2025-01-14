                #leading spaces pyramid

n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for j in range(n):
        if j<n-i:
            print("_",end="")
        else:
            print("*",end=' ')
    print()
