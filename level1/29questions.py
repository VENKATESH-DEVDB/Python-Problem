#Question: Get a four-digit number from user. If the sum of the ten's digit and hundred's digit is
#greater than 10, then print "Success", otherwise print "Failure".

while True:
    n = int(input())
    if n >10000 or n<999:
        print("Enter 4 digit number")
        continue
    break
total = ((n // 10)%10)+((n//100)%10)
if total > 10:
    print("Success") 
else:
    print("Failure")