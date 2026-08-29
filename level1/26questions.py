#Question: Get a two-digit number from user. If the sum of the digits is 10 then print "Success",
#otherwise print "Failure".

while True:
    n = int(input())
    if n >100 or n<=9:
        print("Enter 2 digit number")
        continue
    break

total = (n%10)+(n//10)
if total == 10:
    print("Success") 
else:
    print("Failure")