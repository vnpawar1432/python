str =input("enter the name: ")
print("the name is: ",str)
str1 = (str[::-1])
if(str == str1):
    print("name is palindrom")
else:
    print("name is not palindrom")