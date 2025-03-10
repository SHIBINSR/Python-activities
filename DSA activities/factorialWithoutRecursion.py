number = int(input("enter the number:"))
total = 1

while number >= 1:
    total *= number
    number-=1
print(total)

for i in range(number,0,-1):
    total *= i
print(total)