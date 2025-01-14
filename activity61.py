                 #sum of odd & even digits in a number

n=int(input("enter the numbers:"))
sumodd = 0
sumeven = 0
while n>1:
    y = int(n % 10)
    if y % 2 == 1:
        sumodd += y
    else:
        sumeven += y

    n/=10
print("sum of odd digit:",sumodd)
print("sum of even digit:",sumeven)








