                    #hollow pyramid pattern

# n=int(input("enter the number of rows:"))
# for i in range(n):
#     for j in range(n-i):
#         print('*',end='')
#     for j in range(i):
#         print(' ', end='')
#     for j in range(i):
#         print(' ', end='')
#     for j in range(n-i):
#         print('*', end='')
#     print()

n=int(input("enter the rows:"))
for i in range(n):
    for j in range(n+n):
        if j<n-i or j>i+n-1:
            print('*',end="")
        else:
            print('_',end="")
    print()