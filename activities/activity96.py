          #sum of array

n=int(input("enter the size of an array:"))
a=[]
for i in range(n):
    x=int(input("enter the numbers:"))
    a.append(x)

total=0
for i in a:
    total+=i

print(total)
print(sum(a))