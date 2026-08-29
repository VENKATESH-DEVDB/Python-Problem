#Question: Get a four-digit number from user and only reverse the first two digits of the number,
#then print the number.


rev = 0 
while True:
    n = int(input())
    if n >10000 or n<=999:
        print("Enter 4 digit number")
        continue
    break
while n >100:
    c = n %10
    rev  = rev *10 +c
    n = n//10
else:
    rev = n*100 + rev
    print(rev)