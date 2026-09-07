#Question: Write a program to print the sum of all two-digit odd numbers.

total = 0 
for i in range(10,100):
    if i % 2 !=0 :
        total += i

print(total )