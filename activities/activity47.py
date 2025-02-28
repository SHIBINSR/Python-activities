                     #find the largest of three

s1=int(input("enter the slip 1:"))
s2=int(input("enter the slip 2:"))
s3=int(input("enter the slip 3:"))
if s1>s2 and s1>s3:
    print(s1,"largest number")
elif s2>s1 and s2>s3:
    print(s2,"largest number")
elif s3>s1 and s3>s2:
    print(s3,"largest number")
