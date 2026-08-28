#Question: Get a number from user and subtract 5 from that number if the number is odd, then
#print the result.
main_n = int(input())
odd = [3,5,7,9]
last_digit = main_n%10
bol = last_digit in odd
while bol:

    print(main_n-5)
    break 
else:
    print(main_n)
