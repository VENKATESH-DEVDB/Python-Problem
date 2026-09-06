#Question: Write a program to print the total count of numbers less than 100000 whose
#sum of digits is 14.
count = 0
for i in range(100000):
    sum_digit = 0
    temp = i
    while i >0: 
        c = i %10
        i = i //10
        sum_digit= sum_digit + c
    if sum_digit == 14 :
        count += 1
print(count)