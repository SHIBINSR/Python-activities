             # negative Integers

n=int(input("enter the size of array:"))
a=[]
for i in range(n):
    x=int(input("enter the values:"))
    a.append(x)
c=[]
for i in a:
    if i<0:
        c.append(i)

print(c)

      #or

for i in a:
    if i<0:
        print(i)