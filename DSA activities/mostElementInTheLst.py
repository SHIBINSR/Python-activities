nums = [1, 3, 2, 3, 4, 3, 5, 1, 2, 3, 2]

empty = {}

for i in nums:
    if i in empty:
        empty[i]+=1 
    else:
        empty[i]=1
        
print(empty)

empty_key = 0
empty_value = 0

for i,j in empty.items():
    if j>empty_value:
        empty_value = j
        empty_key = i

print(f"The key:{empty_key} have more elements:{empty_value}")