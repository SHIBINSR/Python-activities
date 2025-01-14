            #Sum of evens!

def sums_of_even(x):
    sum=0
    for i in range(2,x+1,2):
        sum+=i
    return sum

def sum_of_odd(x):
    sum=0
    for i in range(1,x+1):
        if i%2==1:
            sum+=i
    return sum

a=int(input("enter a number:"))
c=sums_of_even(a)
b=sum_of_odd(a)
print(c,b)
