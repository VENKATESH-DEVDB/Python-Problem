#Question: Write a program to get a number from the user and print the total number of digits in that number.

n = int(input())
count = 0 
while n >0:
    n = n //10
    count = count + 1

print(count)