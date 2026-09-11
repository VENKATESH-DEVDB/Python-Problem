#Question: Get a main string and a substring. Check whether the substring is present in
#the main string and print its position.


n = input("enter the string")
c = input("enter the sub string")
search_length = int((len(n)/len(c)))+1
start_search = 0 
end_search = len(c)
for i in range(search_length):
    sub_string = n[i:end_search+i]
    if sub_string == c :
        print(i)
        break 
    
