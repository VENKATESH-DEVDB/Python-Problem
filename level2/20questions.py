#Question: Write a program to print the total number of single-digit prime numbers.
count = 0
for i in range(2,11):
    for j in range(2,i):
        if (i%j)== 0 :
            break 
    else:
        count = count + 1
print (count)
            
             
    