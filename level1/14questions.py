#Question: Get a three-digit number from user and print the reverse of the number.#

rev = 0 
while True:
    n = int(input())
    if n >1000 or n<=99:
        print("Enter 3 digit number")
        continue
    break
while n >0:
    c = n %10
    rev  = rev *10 +c
    n = n//10
else:
    print(rev)