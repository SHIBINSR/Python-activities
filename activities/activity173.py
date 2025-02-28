               #Is it perfect square



def perfect_square(t):
    for i in range(t):
        x=int(input("enter the number find the perfect square:"))
        for i in range(1,x+1):
            s=i**2
            if s==x:
                print(1)  
                break             
        else:
            print(0)
            
    
     

     
a=perfect_square(t=int(input("enter the number of test case:")))
print(a)



 
 