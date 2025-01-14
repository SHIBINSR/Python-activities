                   #percentage and grade

mark1=int(input("enter the subject marks :"))
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
tot=mark5+mark4+mark3+mark2+mark1
per=int((tot/500)*100)
if per>=90:
    print("percentage:",per,"grade:A")
elif per>=80:
    print("percentage:",per,"grade:B")
elif per>=70:
    print("percentage:",per,"grade:C")
elif per>=60:
    print("percentage:",per,"grade:D")
elif per>=50:
    print("percentage:",per,"grade:E")
elif per>=40:
    print("percentage:",per,"grade:F")