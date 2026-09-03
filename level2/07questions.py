#Question: Write a loop program to print the two-digit odd numbers whose sum of digits
#is 7.
n = int(input())

for i in range(16,n):
    if i//10 + i%10 == 7:
        print(i)
