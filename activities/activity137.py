                    #unique element

a = [1, 4, 3, 5, 2, 3, 5, 1, 4]
b=[]
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i]==a[j]:
            count+=1
    if count==1:
        b.append(a[i])

        print("The Unique element is:",b)




