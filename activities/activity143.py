             #Replacing Character

# a=int(input("enter the number of test case:"))
# for i in range(a):
#     s=input(("enter a string:"))

a="restart"
b=''
count=0

for i in a:
    if a[0]==i and count>0:
        b+="$"
        continue
    count += 1
    b+=i



print(b)



