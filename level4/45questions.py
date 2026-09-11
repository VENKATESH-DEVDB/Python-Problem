#Question: Get a number up to 50 digits and reverse it.


Max = 50 
while True:
    n = input()
    if len(n)> Max:
        print (" enter digit only up to 50 digit ")
        continue
    break
int_n = int(n)
rev = 0
while int_n>0:
    rev = rev *10 + (int_n%10)
    int_n //= 10
else:
    print(rev)