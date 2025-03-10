# nums = [10,10,10,20,20,20,20,20]
# nums = [10, 5, 20, 20, 8, 25, 25, 7, 25]
# nums = [10, 10, 10, 10, 10]
nums = [10, 5, 20, 8, 25, 7]
smallest = sec_smallest = float("inf")
for i in nums:
    if i<smallest:
        sec_smallest = smallest
        smallest =i
    elif i<sec_smallest and i!=smallest:
        sec_smallest=i
if sec_smallest == float("inf"):
    print("No second smallest number")
else:
    print(smallest, sec_smallest)
    
print(smallest,sec_smallest)