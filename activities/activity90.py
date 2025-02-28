                        #hollow inverted pyramid pattern

n=int(input("enter the rows:"))
for i in range(n):
    for j in range(n+n):
        if j<i+1  or j>(n+n)-i-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
