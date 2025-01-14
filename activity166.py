#Function 2

         #Power Function

def power_function(a,b):
    c=a**b
    if c>109:
        return "answer is greater than 109!"
    else:
        return c

a=int(input('enter the integer:'))  
b=int(input("enter the power value:"))  

c=power_function(a,b)
print(c)
