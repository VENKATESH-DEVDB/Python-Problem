#Question: Get a string of numbers up to 50 digits and remove all leading zeroes.

Max = 50 
while True:
    n = input()
    if len(n)> Max:
        print (" enter digit only up to 50 digit ")
        continue
    break
print(int(n))