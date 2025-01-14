           #coding Rating

a=int(input("enter the rating:"))
if a>=2100:
    if a%2==1:
        print("grand master")
    else:
        print("GRAND MASTER")
elif a>=1900:
    if a%2==1:
        print("candidate master")
    else:
        print("CANDIDATE MASTER")
elif a>=1600:
    if a%2==1:
        print("expert")
    else:
        print("EXPERT")
elif a>=1400:
    if a%2==1:
        print("pupil")
    else:
        print("PUPIL")
elif a<1400:
    if a%2==1:
        print("newbie")
    else:
        print("NEWBIE")



