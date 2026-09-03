#Question: Write a loop program to print the two-digit even numbers whose sum of digits
#is 6

for i in range(15,61 ):
    if i %2 == 0:
        if i //10 + i%10 == 6 :
            print(i)