                      #palindromic Integer

n=(input("enter the number:"))
j=""
for i in n:
    j=i+j
if j == n:
    print("its palindrome")
else:
    print("not palindrome")


#           (or)


# a=n[::-1]
# if a==n:
#     print("palindrome")
# else:
#     print("not palindrome")









