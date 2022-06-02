str = input("enter the string: ")
str1 = "!@#$%^&*()_+."
str2 = ""
for i in str:
    if i in str1:
        pass
    else:
        str2 = str2+i
print(str2)