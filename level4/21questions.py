#Question: Write a program to print the total number of two-digit prime numbers.
count = 0 
for i in range(11,100,2):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break 
    else :
        count += 1 
print(count)