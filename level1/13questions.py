#Question: Get a two-digit number from user and print the reverse of the number.#
rev = 0 
while True:
    n = int(input())
    if n >100 or n<=9:
        print("Enter 2 digit number")
        continue
    break
while n >0:
    c = n %10
    rev  = rev *10 +c
    n = n//10
else:
    print(rev)