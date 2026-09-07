#Question: Print the largest three-digit prime number.
curentprim = 0 
prevprime =97 
for i in range(999,99,-1):
    for j in range(2,int(i**0.5)+1):
        curentprim = i 
        if i%j == 0:
            
            break 
    else :
        print(i)
        break