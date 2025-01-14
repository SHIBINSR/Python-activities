                   #Rows  & Column Sums.

a=[[1,2],[4,5],[8,9],]
b=[]

for i in range(len(a)):
    sum=0
    for j in range(len(a[i])):
        sum+=a[i][j]
    b.append(sum)

sum=0
sum1=0

for i in range(len(a)):
    for j in range(len(a[i])-1):
        sum+=a[i][j]
    for j in range(1,len(a[i])):
        sum1+=a[i][j]

b.append(sum)
b.append(sum1)

print(b)
