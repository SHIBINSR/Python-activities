# Input: [3, 7, 2, 9, 1]
# Output: 9

# Input: [-5, -2, -8, -1]
# Output: -1
  #max element
input = [3,7,2,9,1]
a=input[0]
for i in input:
    if i>a:
        a=i
print(a)


  #min element
input = [3,7,2,9,1]
a=input[0]
for i in input:
    if i<a:
        a=i
print(a)