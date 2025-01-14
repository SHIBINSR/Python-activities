                    #palindrome or Not

t=int(input("enter the test case:"))

for i in range(t):
    a=input("enter the element:")
    b=''
    for i in a:
        b=i+b
    if b == a:
        print(True)
    else:
        print(False)