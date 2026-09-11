#Question: Get a string and a character from the user. Find all positions where the
#character is present and print them.

n = input("enter the string")
c = input("enter the char to be searched")
apperance = []
for i in range(len(n)) :
    if n[i] == c :
        apperance.append(i)
else:
    print(apperance)