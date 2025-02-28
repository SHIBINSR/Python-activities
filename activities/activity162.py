        #find the ceil value

from math import ceil

def ceil_value(a):
    x=a/200
    return ceil(x)       

a=ceil_value(a=int(input("enter the value:")))
print(a)    