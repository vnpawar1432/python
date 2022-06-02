str  = input("enter the string: ")
count = 0
vowels = ("aeiouAEIOU")
for i in str:
    if i in vowels:
        count = count+1
print(count)