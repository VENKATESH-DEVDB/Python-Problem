#Question: Get a four-digit number from the user and print its reverse.

while True :
    n = int(input())
    if n > 10000 or n <999:
        print("Enter a 4 digit number")
        continue
    break
rev = 0 
while n > 0 :
    c = n %10 
    n  = n // 10 
    rev = rev * 10 + c 
else : print(rev)