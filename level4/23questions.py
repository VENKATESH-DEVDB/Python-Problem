#Question: Write a program to print the sum of single-digit prime numbers.

total = 0
for i in range(2,10 ):
    for j in range(2,i):
        if i%j == 0:
            break 

    else:
            total +=i
print(total)