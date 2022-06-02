str = input("enter the string: ")
for i in str:
    if(i.isdigit()):
        str = str.replace(i,'',)
print(str)