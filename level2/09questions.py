#Question: Write a loop program to print the sum of two-digit numbers whose one's digit is 5.
total = 0 
for i in range(10 , 100):
    if i %10 == 5:
        total = total + i

print(total)