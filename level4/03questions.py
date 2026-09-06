#Question: Get a three-digit number from the user and print the digit in the one's position.

while True:
    n = int(input())
    if n > 1000 or n < 99:
        print(" Enter a three digit number")
        continue
    break
print(n%10 )