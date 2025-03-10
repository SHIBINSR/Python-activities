  #largest

lst = [1,2,3,4,5,6,7]
num=int(input("Enter the kth element:"))
if num > len(lst):
    print("Not enough elements")
else:
    for _ in range(num):
        larget =lst[0] 
        for val in lst:
            if val > larget:
                larget = val
        lst.remove(larget)
    print(larget)
    
  #smallest

lst1= [1,2,3,4,5,6,7]
num=int(input("Enter the kth element:"))
if num > len(lst1):
    print("Not enough elements")
else:
    for _ in range(num):
        smallest = lst1[0]
        for i in lst1:
            if i < smallest:
                smallest = i
        lst1.remove(smallest)
    print(smallest)

