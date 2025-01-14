             #Frequency count

a=[1,2,5,1,5,1]
b=[]

      ########

for i in (a):
    count=0
    for j in (a):
        if i==j:
            count+=1
    b.append(count)

#          or

# for i in range(len(a)):
#     count=0
#     for j in range(len(a)):
#         if a[i]==a[j]:
#             count+=1
#     b.append(count)

       #############

print(b)