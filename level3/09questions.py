#Question: Get a two-digit number from user and swap the digits.

while True:
    n = int(input())
    if n > 100 or n <9:
        print("Enter a two digit number")
        continue
    break 
def swap (a):
    swap_num = 0 
    c = a%10
    a = a//10 
    swap_num = ( c )*10 + a
    return swap_num 
print(swap (n))