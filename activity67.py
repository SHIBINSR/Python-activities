                      #calculate the steps

n=int(input("enter the value:"))
temp=n
count=0

while temp>1:
    count +=1
    temp//=2

print(count)