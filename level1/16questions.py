#Question: Get a four-digit number from user and only reverse the last two digits of the number,
#then print the number.


rev = 0 
while True:
    n = int(input())
    if n >10000 or n<=999:
        print("Enter 4 digit number")
        continue
    first_two = n//100
    last_two = n %100
    break

while first_two > 0:
    c = first_two%10
    rev = rev*10 + c 
    first_two = first_two//10 
else:
    rev = rev*100 + last_two
    print(rev)