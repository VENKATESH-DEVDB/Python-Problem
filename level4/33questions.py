#Question: Print the total number of non-decreasing numbers from 1000 to 9999. A
#non-decreasing number has digits that do not decrease from left to right



count =  0 
pow= 4
for i in range(1000,10000):
    bol = True
    while i > 0 :
        if (i%10)<((i//10)%10):
            bol = False
            break 
        i //=10
    if bol :
        count+=1
else:
    
    print(count)

