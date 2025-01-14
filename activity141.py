              #Concatenate strings-Easy

a=input("enter two string with space:").split()
result=""
for i in a:
    if i==" ":
        continue
    result+=i
print(result)