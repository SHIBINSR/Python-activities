n=int(input("enter a number:"))
i=1
while i<=n:
    j=i**2
    if j>n:
        break
    print(j,end="\t")
    i+=1



