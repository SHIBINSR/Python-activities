# nums = [10,10,10,20,20,20,20,20]
# nums = [10, 5, 20, 20, 8, 25, 25, 7, 25]
nums = [10, 10, 10, 10, 10]
largest = second_largest  = float('-inf')

for i in nums:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
    	second_largest = i
   
    
print(largest,second_largest)
