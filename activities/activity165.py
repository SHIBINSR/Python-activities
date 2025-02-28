            #Time to end corona

def corons_calc(a,b):
    d=b+b
    return d-a


a=int(input("enter the average cases recovered per day:"))   
b=int(input("Number of new cases per day:")) 
c=int(input("current active cases of corona:"))        

x=corons_calc(a,b)
print(x)