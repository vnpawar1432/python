# Sum of number digits in List
list = [12,36,54,98,62]
list1 = []
for i in list:
    Sum = 0
    for j in str(i):
        Sum += int(j)
    list1.append(Sum)
print(str(list1))




