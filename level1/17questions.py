#Question: Get a two-digit number from user and make the one's digit as 0, then print it.
 

while True:
    n = int(input())
    if n >100 or n<=9:
        print("Enter 2 digit number")
        continue
    break

if n > 0:
    c = n //10
    print (c*10)
    

    
