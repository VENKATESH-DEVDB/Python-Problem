#Question: Print the number of zeroes encountered between 0 and 1000.
count = 0 
for i in range(0,1000+1):
    while i >  0:
        
        if i%10 == 0: 
            count +=1
        i  = i //10 
else :
    print(count)