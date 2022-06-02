str = input("enter the string: ")
str1 = str.lower()
count = 0
set = ("aeiuo")
for i in str1:
    if i in set:
        count +=1
    else:
        pass
print(count)