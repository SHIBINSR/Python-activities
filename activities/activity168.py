         #Volume of Sphere

from math import ceil

def vol_sphere(r):
    a=((4*3.14*r**3)/3)
    return ceil(a)

volume=vol_sphere(r=int(input("enter the radius of sphere:"))) 
print("the volume of sphere is :",volume)