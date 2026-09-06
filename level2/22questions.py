#Question: Write a program to get a number from the user and print the total number of
#two-digit odd numbers in the number.


n = int(input())
count =0
while n> 0:
    c = n %100
    n = n // 10
    if c >9 :
        print(c)
        if c %2 !=0:
     
            count = count + 1
else :
    print(count)