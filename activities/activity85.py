                   #skip even numbers half pyamid

n=int(input("enter the rows:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2==1:
            print(j,end="\t")
        elif j%2==0:
            print("_",end="\t")
    print()