                #Largest in each Row of 2D Array.

R = int(input("enter the rows:"))
C = int(input("enter the cols:"))
mat=[]

for i in range(R):
    mat.append([])
    for j in range(C):
        x=int(input("enter the values:"))
        mat[i].append(x)

print(mat)
result=[]

for i in mat:
    result.append(max(i))

print(result)