                   #Quadrant Number

x=int(input("enter the X coordinates:"))
y=int(input("enter the Y coordinates:"))
if x>0 and y>0:
    print("X,Y belongs to first quadrant")
elif x>0 and y<0:
    print("X,Y belongs to second quadrant")
elif x<0 and y<0:
    print("X,Y belongs to third quadrant")
elif x<0 and y>0:
    print("X,y belongs to fourth quadrant")