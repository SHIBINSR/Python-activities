                #which Triangle

a=int(input("enter three sides of triangle:"))
b=int(input())
c=int(input())

if a==b==c:
    print("equilateral triangle")
elif a!=b!=c:
    print("scalene triangle")
else:
    print("isoceles triangle")
