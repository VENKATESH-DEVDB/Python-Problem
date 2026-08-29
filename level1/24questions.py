#Question: Get a three-digit number from user and subtract 5 from that number if one's digit and
#hundred's digit are the same, then print the result

while True:
    n = int(input())
    if n >1000 or n<=99:
        print("Enter 3 digit number")
        continue
    break
ones_digit = n % 10 
hund_digit = n //100
bol = (ones_digit == hund_digit)
while bol:
    print(n - 5)
    break
else:
    print(n)