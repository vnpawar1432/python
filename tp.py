str = input("enter the string: ")
s = {}
for i in str:
    if i in s:
        s[i] +=1
    else:
        s[i] = 1
for i in str:
    if s[i] != 0:
        print("{}{}".format(s[i],i),end="")
        s[i] =0
