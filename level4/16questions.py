#Question: Write a program to print the total number of three-digit odd number

count = 0 
for i in range(100,1000):
    if i % 2 != 0 :
        count+=1
print(count)