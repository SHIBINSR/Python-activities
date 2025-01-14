              # is it prime?

n = int(input("enter the number:"))
count=0
for i in range(2, n):
    if n%i==0:
        count+=1

if count==0:
    print("prime")
else:
    print("not prime")


            #printing all prime numbers in given number.

x=int(input("enter the number:"))

for i in range(2,x+1):
    count=0

    for j in range(1,i+1):
        if i%j==0:
            count +=1

    if count<=2:
        print(i)
