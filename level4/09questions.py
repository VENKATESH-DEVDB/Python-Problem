#Question: Get a two-digit number from the user and print the sum of all digits.


while True:
    n = int(input())
    if n > 99 or n < 9 :
        print("enter a 2 digit number")
        continue
    break

total = ((n %10))+(n//10)
print(total)