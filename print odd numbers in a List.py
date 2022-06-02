list = [78,65,42,36,15,2,8,4,89,8,65]
list1 = []
for i in list:
    if(i%2==1):
        list1.append(i)
        print(i,end=" ")
print(list1)