#Question: Print the smallest three-digit prime number.

for i in range(100,1000,):
    for j in range(2,int((i ** 0.5)+1)):
        if i%j == 0 :
            break
    else:
        print(i)
        break 
    