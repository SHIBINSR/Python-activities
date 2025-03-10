my_dict = {}
z=input("how much elelment do you want")
for i in range(len(z)):
    a=input('enter the key')
    b=input("enter the value")
    my_dict[a]=b
print(my_dict)

my_dict1 = {}
keys = ['a', 'b', 'c']
values = [1, 2, 3]
for key, value in zip(keys, values):
    my_dict1[key] = value
print(my_dict1)

my_dict2 = {}
keys = ['a', 'b', 'c']
values = [1, 2, 3]
for i in range(len(keys)):
    my_dict2[keys[i]] = values[i]
print(my_dict2)

for i in my_dict1:
    print(i)
print()
for i in my_dict1.keys():
    print(i)
print()
for i in my_dict1.values():
    print(i)
print()
for i in my_dict1.items():
    print(i)
print()
for i,j in my_dict1.items():
    print(i,j)
print()
for i in range(len(my_dict1.keys())):
    print(my_dict1.items())
