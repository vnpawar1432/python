str = input("String: ")
str1 = str.lower()
count = 0
set = ("aeiou")
for i in str1:
    if i in set:
        count +=1
if(count==0):
    print("vowels is not present")
else:
    print("vowels is  present")