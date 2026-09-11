#Question: Add two integer arrays of up to 50 digits and store the result in a 51-digit array.


import numpy as np

Max = 50 
while True:
    n1 = input()
    if len(n1) > Max:
        print(" enter digit only up to 50 digit ")
        continue
    break

while True:
    n2 = input()
    if len(n2) > Max:
        print(" enter digit only up to 50 digit ")
        continue
    break

num1 = int(n1)
num2 = int(n2)
total = num1 + num2
arr = np.array([int(i) for i in str(total)])



print(arr)
