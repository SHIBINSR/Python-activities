        #is it perfect

t=int(input("enter the test case:"))
for i in range(t):
    n=int(input("enter the number:")) 
    p=0
    for i  in range(1,n):
        if n%i==0:
            p+=i           
 
    if p==n:
        print("its perfect")
    else:
        print("its not perfect")

    








