               #Count of primes.


def count_primeNumber(a):
    for i in range(2,a+1):
        count=0

        for j in range(1,i+1):

            if i%j==0:

                count +=1

        if count<=2:
            print(i) 
   
            
n=int(input("enter the number:"))
count_primeNumber(n)
    

