#Question: Write a program to print the total number of single-digit prime numbers.
#Assume 0 and 1 are not prime.
count = 0
for i in range(2,10 ):
    for j in range(2,i):
        if i%j == 0:
            break 

    else:
            count +=1
print(count)