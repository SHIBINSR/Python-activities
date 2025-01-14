                  #max and min of an array

n=int(input("enter the lenght of array:"))
a=[]
for i in range(n):
    x=int(input("enter the numbers:"))
    a.append(x)

print(max(a),min(a))