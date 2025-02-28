                #Divisible by 5 and 7

a=[23,34,25,35,66,70,14]
b=[]
      ##############

for i in range(len(a)):
    if a[i]%5==0 and a[i]%7==0:
        b.append(a[i])

#             (or)

for i in a:
    if i%5==0 and i%7==0:
        b.append(i)

      ############

print(b)