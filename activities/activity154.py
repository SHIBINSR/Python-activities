                  #vowels vs consonants

t=int(input("enter the number of test cases:"))
for i in range(t):
    s=input("enter the string:")
    vowels=0
    consonants=0
    for i in s:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            vowels+=1
        else:
            consonants+=1
    print("vowels =",vowels,"consonants =",consonants)