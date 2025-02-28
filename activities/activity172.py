                #BMI Calculator

def bmi_cal(h,w):    
    y=h/100    
    bmi=w/(y*y)
    
    if bmi<18.5:
        print("under weight")
        return round(bmi,2)

    elif bmi>=18.5 and bmi<=24.9:
        print("normal Weight")
        return round(bmi,2)

    elif bmi>24.9 and bmi<=29.9:
        print("over weight")
        return round(bmi,2)

    else:
        print("Obese")
        return round(bmi,2)

h=int(input("enter the Height of the person:"))
w=int(input("enter the Weight of tht person:"))

d=bmi_cal(h,w)
print(d)
