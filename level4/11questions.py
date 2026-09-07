#Question: Get a four-digit number from the user and print the sum of all digits.


while True:
    n = int(input())
    if n > 10000 or n < 999 :
        print("Enter a 4 digit number")
        continue
    break
total =  0 
while n > 0 :
     c = n %10 
     n = n // 10 
     total += c 
else:
     print(total)