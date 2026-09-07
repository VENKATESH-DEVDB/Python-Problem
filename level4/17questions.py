#Question: Write a program to print the sum of all single-digit odd numbers.

total = 0 
for i in range(0,10):
    if i % 2 !=0 :
        total += i

print(total )