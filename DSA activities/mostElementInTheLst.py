nums = [1, 3, 2, 3, 4, 3, 5, 1, 2, 3, 2]

empty = {}

for i in nums:
    if i in empty:
        empty[i]+=1 
    else:
        empty[i]=1
        
print(empty)

key = 0
value = 0

for i,j in empty.items():
    if j>value:
        value = j
        key = i

print(f"The key:{key} have more elements:{value}")