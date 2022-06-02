# list = [1,2,3,4,5,6]
# list2 = list
# print(list2)

def copy(list):
    list2 = list[:]
    return list2
list = [1,2,3,4,5]
print(copy(list))