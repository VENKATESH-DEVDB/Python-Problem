#Question: Write a program to get a number from the user and print the reverse of that number.

n = int(input())

rev = 0 
while n>0:
    c = n %10
    rev = rev *10 + c
    n = n //10

print(rev)