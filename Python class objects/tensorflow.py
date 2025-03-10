# a=input("enter a string:")
# b=""
# for i in a:
#     b=i+b

# print(b)
# a="1,3,5,6,7"
# b="2,4,6,8,10"
# c=a
# a=b
# b=c

# print(a)
# print(c)
          
# n="shibin"
# for i in (n):
#     for j in (n):
#         if i==j:
#             print(i,end="")
#         else:
#             print(" ",end="")
#     print()

        #leap year
# n=int(input("enter the year:"))
# if n%4==0 and n%100==0 or n%400==0:
#     print("its leap year:")
# else:
#     print("its not leap year")


#        #Amstrong number
# n=int(input("enter the number:"))
# b=n
# a=str(n)
# count=0
# for i in a:
#     count+=1
# y=0
# while b>=1:
#     z=b%10
#     y+=z**count
#     # y.append(z**count)
#     b//=10
# if n==y:
#     print(f"{n} it is a amstrong number")
# else:
#     print(f"{n} it not a amstrong number")


        #sum of natural numbers in pattern
n = int(input("enter the number: "))
for i in range(1,n+1):
    a = []
    for j in range(1,i+1):
        print(j, end="")
        if(j < i):
            print("+", end="")
        a.append(j)
    print(f"={sum(a)}")
 

