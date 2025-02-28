               #convert celsius to Farenheit

t=int(input("enter the number of test case:"))

for i in range(t):
    def cel_farenheit(x):
        return (x*9/5)+32

    a=cel_farenheit(x=float(input("enter the temperature in degree celsius:")))
    print(a,"'F")
    