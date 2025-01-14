            #Copy the array

A=[]
n=int(input("eneter the size of array:"))
for i in range(n):
    x=int(input("enter the values:"))
    A.append(x)
print(A)
m=int(input("enter the value of adding:"))
B=[]
for i in A:
    B.append(i+m)

print(B)


