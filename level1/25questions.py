#Question: Get a four-digit number from user and subtract 5 from that number if ten's digit
#position and hundred's digit position are the same, then print the result

while True:
    main_n = int(input())
    n = main_n
    if n >10000 or n<=1000:
        print("Enter 4 digit number")
        continue
    break
first_two_digit = n //100
last_two_digit = n %100

bol = ((first_two_digit%10)==(last_two_digit//10))
while bol:
    print(n - 5)
    break
else:
    print(n)