#Question: Get a two-digit number from user and make the ten's digit 1, then print it.
while True :
    n = int(input())
    if n>100 or n<=9:
        print("enter a 2 digit number")
        continue
    break 
if n > 0 :
    c = n%10
    print(10+c)