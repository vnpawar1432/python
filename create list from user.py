s = input()
li = []
for i in s:
    if(i==" "):
        pass
    else:
     li.append(i)
print(li)


# list convert into string
str = "".join(li)
print(str)
# string convert into list
l1 = str.split(" ")
print(l1)
