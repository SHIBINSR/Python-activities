                # some patterns

n=int(input("enter the number:"))
for i in range(n):
    if i<1 or i>n-2:
        for j in range(n):
            print("*",end="")
    else:
        for j in range(n):
            if j<1 or j>n-2:
                print("*",end="")
            else:
                print(" ",end="")
    print()

           #(or)

n=int(input("enter the row:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()


    ##############           

x=int(input("enter the row:"))
for i in range(1,x+1):
    for j in range(i*3):
        print("*",end="\t ")
    print()
    for j in range(2):
        print("*")

           #########

n=int(input("enter :"))
for i in range(n):
    for j in range(n):
        if j==i or j==n-i-1:
            print("*",end="\t")
        else:
            print(" ",end="\t")
    print()

            ###########

 



    