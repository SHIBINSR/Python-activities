                  #sum of odd & even index digit in a number

n=int(input("enter the numbers:"))

temp=n
count=0

while temp>=1:
    count+=1
    temp/=10

sum_of_odd=0
sum_of_even=0

while count>=0:
    if count%2==1:
        x=int(n%10)
        sum_of_odd+=x
    elif count%2==0:
        x=int(n%10)
        sum_of_even+=x
    n /= 10
    count-=1

print("sum of odd index digit:",sum_of_odd,'\n'"sum of even index digit:",sum_of_even)




