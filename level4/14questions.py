#Question: Write a program to print the total number of single-digit odd numbers.
count = 0 
for i in range(0,10):
    if i % 2 !=0 :
        count += 1

print(count)