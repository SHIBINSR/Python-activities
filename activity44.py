              #music certification

n=int(input("enter the number of album sold:"))
if n>=500000 and n<1000000:
    print("gold")
elif n>=1000000 and n<10000000: 
    print("platinum")
elif n>=10000000:
    print("diamond")
else:
    print("None")