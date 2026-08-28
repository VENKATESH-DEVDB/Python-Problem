#Question: Get a two-digit number from user and make the one's digit as 0, then print it.
 
rev = 0 
while True:
    n = int(input())
    if n >100 or n<=10:
        print("Enter 4 digit number")
        continue
    break

if n > 0:
    c = n //10
    print (c*10)
    

    
