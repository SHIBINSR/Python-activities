                #leading spaces inverted pyramid

n=int(input("enter the number of rows:"))

for i in range(n):
    for j in range(n):
        if j<i:
            print("_",end="")
        else:
            print("*",end="")
    print()