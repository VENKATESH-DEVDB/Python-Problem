#Question: Write a loop program to print the two-digit odd numbers whose sum of digits
#is 7.

for i in range(16,71):
    if i %2 != 0:
        if i//10 + i%10 == 7:
            print(i)
