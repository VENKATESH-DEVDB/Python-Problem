#Question: Get a number from user and check whether it is prime or not, then print the
#result.

n = int(input())
def prime(a):
    if a == 0 or a == 1 or n == 2 :
        return " enter a greater number"
    elif n % 2 == 0:
        return "not a prime"
    else :
        for i in range(3,int(a**0.5)+1):
            if a % i == 0 :
                return "not prime"
            else : 
                return "prime"
print(prime(n))