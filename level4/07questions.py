#Question: Get a three-digit number from the user and print its reverse.

while True:
    n = int(input())
    if n > 1000 or n < 99:
        print(" Enter a three digit number")
        continue
    break


def revers(a):
    rev = 0 
    while a>0:
        c = a %10 
        a = a//10
        rev = rev * 10 + c 
    else :
        return rev 
print(revers(n))