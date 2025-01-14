                   #pac-man

a=int(input("if the pac-man has power pellet enter 1 for yes else enter 0:"))
if a==1:
    b=int(input("if pac-man touch the ghost if yes press 1 else 0:"))
    if b==1:
        print(0)
    else:
        print(1)
else:
    print(0)