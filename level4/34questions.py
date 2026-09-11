#Question: Print the total number of palindrome numbers less than 100000.
count = 0 
for i in range(11,100000):
    if i %10 == 0 :
        continue
    temp = i 
    rev = 0 
    while temp > 0:
        rev = rev *10 + (temp%10)
        temp //=10
    else:
        if rev == i :
            count +=1
else:
    print(count)