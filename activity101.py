                #Difference of even and odd

a=int(input("enter the no of test case:"))
for i in range(a):
    b=[56,63,87,24,32,13,15,19,44,52]

odd=0
even=0
for i in b:
    if i%2==1:
        odd+=i
    else:
        even+=i
print(int(even-odd))