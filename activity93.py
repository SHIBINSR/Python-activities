                     #full pyramid

n=int(input("enter the number:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")

    print()





# ____*____
# ___*_*___
# __*_*_*__
# _*_*_*_*_
# *_*_*_*_*


