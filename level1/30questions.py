#Question: Get a four-digit number from user. If the sum of the ten's digit and hundred's digit is
#equal to 10, and one of the digits is more than 7 then print "Success", otherwise print "Failure".

while True:
    n = int(input())
    if n >10000 or n<999:
        print("Enter 4 digit number")
        continue
    break
ten_degit = ((n//10)%10)
hund_digit = ((n//100)%10)
total = ten_degit+hund_digit
bol = (  ten_degit > 7 or hund_digit>7 ) 
if  bol and (total == 10):
    print("Success") 
else:
    print("Failure")