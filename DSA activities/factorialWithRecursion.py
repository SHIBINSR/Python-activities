def recursion(n):
    if n == 0:
        return 1  
    a= n* recursion(n-1) 
    return a
number = int(input("enter the number"))
print(recursion(number))