                #First Occurrence

a=input("enter the elments:")
b=int(input("enter the ascii code:"))
c=chr(b)
d=""
for i in range(len(a)):
    if a[i]==c:
        d=i
        break

if c not in a:
    print(-1)
else:
    print(d)






