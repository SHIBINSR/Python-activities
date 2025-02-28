          #Situation of Number

n=int(input("enter the number:"))
if n>0 and n%2==1:
    print("number is positive and odd")
elif n>0 and n%2==0:
    print("number is positive and even")
elif n<0 and n%2==1:
    print("number is negative and odd")
elif n<0 and n%2==0:
    print("number is negative and even")

