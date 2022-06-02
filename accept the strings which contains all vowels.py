# accept the strings which contains all vowels

str = input("Enter string: ")
str = str.lower()
vowels = ("aeiou")
s = set({})
for i in str:
    if i in vowels:
        s.add(i)
    else:
        pass
if len(vowels) == len(s):
    print("homo")
else:
    print("not homo")
