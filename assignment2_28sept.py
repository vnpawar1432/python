str1 = input("enter the string:  ")
list1 = []
# list2 = []
count = 0
str2 = str1.split()
for x in str2:
    if (x.isdigit()):
        list1.append(int(x))
        list1.sort()
        count = 1

if(count==1):
    print(",".join(map(str,list1)))
else:
    print("None found")


# print(list2)

