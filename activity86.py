            #inverted half pyramid
            
n=int(input("enter the rows:"))
for i in range(n):
    for j in range(n-i):
        print("*",end="\t")
    print()