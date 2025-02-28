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
            
n=int(input("enter the number:"))
for i in range(n):
    for j in range(n):
        if i<1 or i>n-2 or j<1 or j>n-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
            #(or)

n=int(input("enter the row:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()


    ##############           

x=int(input("enter the row:"))
for i in range(1,x+1):
    for j in range(i*3):
        print("*",end="")
    print()
    if i==x:
        continue 
    else:
        print("*")
        print("*")

           #########

n=int(input("enter :"))
for i in range(n):
    for j in range(n):
        if j==i or j==n-i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

            ###########

 



    