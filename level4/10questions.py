#Question: Get a three-digit number from the user and print the sum of all digits.

while True:
    n = int(input())
    if n > 1000 or n < 99 :
        print("Enter a 3 digit number")
        continue
    break

totsl = (n%10 )+ ((n//10 )%10) + (n//100)
print(totsl)