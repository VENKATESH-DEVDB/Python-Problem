#Question: Get a two-digit number from the user and print its reverse

while True:
    n = int(input())
    if n >100 or n <9 :
        print("Enter a two digit number")
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