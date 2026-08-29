#Question: Get a three-digit number from user. If the sum of the digits is less than 10, then print
#the sum, otherwise add the digits of the sum and continue until the result is a single digit.
total = 0 
while True:
    n = int(input())
    if n >1000 or n <=99:
        print("enter a 3 digit number")
        continue
    break
while n>0 :
    c = n % 10 
    total = total +c
    n = n//10
    if n == 0:
        if total <10:
            print(total)
        else :
            n = total
            total = 0 
