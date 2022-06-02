str = input("enter the string: ")
str1 = str.lower()
SET = ("aeiou")
s = set({})
for i in str1:
    if i in SET:
        s.add(i)
    else:
        pass
if(len(SET)==len(s)):
    print("accept")
else:
    print("not accepted")