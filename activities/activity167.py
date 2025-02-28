        #area of the circle

from math import ceil

def area_circle(r):
    b=3.14*r**2
    return ceil(b)

area=area_circle(r=int(input("enter the radius of circle:")))
print("area of circle is:",area)