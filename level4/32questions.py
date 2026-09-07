#Question: Print the total number of prime numbers below 1,000,000 whose sum of digits is equal to 14.

count = 0 
for i in range(1000000): 
    if i < 2:
        continue
        
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break 
    else:
        total = 0
        temp = i 
        while temp > 0:
            total += temp % 10
            temp = temp // 10
        
        if total == 14:
            count += 1
print(count)
