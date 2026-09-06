#Question: Write a program to get a number from the user and print the total number of
#single-digit prime numbers in the number.

n = int(input())
count = 0 
prime = [2,3,5,7]
while n > 0 :
    c = n %10
    n = n // 10 
    if c in prime :
        count  = count + 1
else :
    print(count)