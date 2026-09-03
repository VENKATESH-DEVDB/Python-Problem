#Question: Write a program to get a number from the user and print the sum of all digits.


n = int(input())
total  = 0
while n >0:
    c= n %10 
    n = n // 10
    total = total + c
print(total)