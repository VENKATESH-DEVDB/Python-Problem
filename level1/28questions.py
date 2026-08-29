#Question: Get a three-digit number from user. If the sum of the one's digit and hundred's digit is
#less than 10, then print "Success", otherwise print "Failure".

while True:
    n = int(input())
    if n >1000 and n<=99:
        print("Enter 3 digit number")
        continue
    break
total = (n % 10)+(n//100)
if total < 10:
    print("Success") 
else:
    print("Failure")