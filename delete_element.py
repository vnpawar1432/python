# delete element by using del
My_list = [1,2,3,4]
print(My_list)
del My_list[2]
print(My_list)

del My_list[1:3]
print(My_list)

#delete element by remove,pop and clear
My_list = [1,2,3,4,5,6,7,8,9]
My_list.remove(9)
print(My_list)
My_list.pop(0)
print(My_list)
My_list.clear()
print(My_list)