                #sum of columns of 2D array

# for i in a:
#     for j in i:
#         print(j)

    #(or)

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j])

       ###############################################################

# row = int(input("enter the number of rows:"))
# col = int(input("enter the number of column:"))
# mat = []
# for i in range(row): #for creating inner list
#     mat.append([])   #for adding a list to the matrix that is row ,col.
# for i in range(row): #for row
#     for j in range(col): #for col
#         x=int(input("enter the values:"))
#         mat[i].append(x) #will add the elements to the list
# print(mat)

#            (or)

# row=int(input("enter the row:"))
# col=int(input("enter the col:"))
# mat=[[int(input("enter the elements:")) for i in range(col)] for j in range(row)]
# print(mat)
# for i in range(len(mat)):
#     s=[]
#     for j in range(len(mat[i])):
#
#         print(mat[i][j])

       #####################################

row=int(input("enter the size of row:"))
col=int(input("enter the size of column:"))
mat=[]

for i in range(row):
    mat.append([])
    for j in range(col):
        x=int(input(f"enter the mat[{i}][{j}] values:"))
        mat[i].append(x)

print(mat)

result=[]
for i in range(col):
    result.append([])

for i in range(col):
    a=0
    for j in range(row):
        a+=mat[j][i]
    result[i].append(a)

print(result)






