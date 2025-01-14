           #square root of a number.

from math import sqrt
def square_root(a):
    b=int(sqrt(a))
    if b**2==a:
        return b
    else:
        return -1
        


x=int(input("enter a number:"))
y=square_root(x)
print(y)