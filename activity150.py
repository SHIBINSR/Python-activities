                     #Last Occurrence

a=input("enter the elements:")
b=int(input("enter the ascii code:"))
c=chr(b)

d=""
for i in range(len(a)):
    if c==a[i]:
        d=i
        

if c not in a:
    print(-1)
else:
    print(d)


    