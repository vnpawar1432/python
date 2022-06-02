a = [1,2,3,4,5]
b = [4,5,6,7,8]
for i in a[:]:
    if i in b:
        a.remove(i)
        b.remove(i)

print("list1 : ", a)
print("list2 : ", b)
