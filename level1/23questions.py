#Question: Get a two-digit number from user and subtract 5 from that number if the sum of the
#digits of the number is odd, then print the result. 


odd = [3,5,7,9]
while True:
    main_n = int(input())
    n = main_n
    if n >100 or n<=99:
        print("Enter 2 digit number")
        continue
    break

c = n %10
n = n//10
total = c + n 
bol = (total%10) in odd 
while bol :
    print(main_n-5)    
    break 
else:
        print(main_n)
 