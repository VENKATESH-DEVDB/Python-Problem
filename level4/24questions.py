#Question: Write a program to print the sum of all two-digit prime numbers.


total = 0
for i in range(11,100,2 ):
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            break 

    else:
            total +=i
print(total)