       #find the floor value

from math import floor


def floor_value(a):
    x=a/200 
    return floor(x)

a=floor_value(a=int(input("enter the number:")))
print(a)