# check if a string has at least one letter and one number
str = input("enter string: ")
for i in str:
    if(i.isdigit()):
        flag1 = True
    else:
        flag1 = False
    if(i.isalpha()):
        flag2 = True
    else:
        flag2 = False

print(flag1,flag2)