             #sum of odds-easy

a=int(input("enter the positive number:"))
sum=0
for i in range(1,a+1):
    if i%2==1:
        sum+=i
print(sum)