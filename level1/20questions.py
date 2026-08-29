#Question: Get a three-digit number from user and make the ten's digit as 0, then print i
while True:
    n = int(input())
    if n >1000 or n<=99:
        print("enter a 3 digit number")
        continue
    break 
if n > 0:
    c = n //100
    c = c*100
    last_digit=n %10
    print(c+last_digit) 