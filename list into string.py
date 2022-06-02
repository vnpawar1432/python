inp = int(input("Enter the size of list: "))
list1 = []
for i in range(0,inp):
    element = int(input("Enter element in list:  "))
    list1.append(element)
print(list1)
print(sum(list1))
map(str,list1)
str1 = " ".join(map(str,list1))
print(str1)