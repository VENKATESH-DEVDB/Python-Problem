#Question: Get a three-digit number from user and make the one's digit as 2, then print it
while True:
    n = int(input())
    if n >1000 or n<=99:
        print("enter a 3 digit number")
        continue
    break 
if n > 0:
    c = n //10
    print((c*10) + 2 )