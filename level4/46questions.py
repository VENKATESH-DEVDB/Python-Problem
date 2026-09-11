#Question: Get a number string up to 50 digits and convert it into an integer array.
import numpy as np 
Max = 50 
while True:
    n = input()
    if len(n)> Max:
        print (" enter digit only up to 50 digit ")
        continue
    break
arr = np.array([int(i) for i in n])


print(arr)