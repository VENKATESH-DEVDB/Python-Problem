#Question: Print the total number of prime numbers below 1,000,000 whose sum of digits is equal to 14.

limte = 1000000

is_prime = [True] * limte
is_prime[0] = is_prime[1] = False

for i in range(2, int(limte**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, limte, i):
            is_prime[j] = False

count = 0
for i in range(2, limte):
    if is_prime[i]:
        if sum(map(int, str(i))) == 14:
            count += 1

print(count)  
