#add element in list by using indexed

My_list = [1,2,3,4]
print(My_list)
My_list[0] = 3
print(My_list)
My_list[1:4] = [4,5,6]
print(My_list)

#add element by append and extend

My_list = [1,2,3,4]
print(My_list)
My_list.append(5)
print(My_list)
My_list.extend([6,7,8,9,10])
print(My_list)

# add element by using + (concatination)
My_list = [1,2,3,4]
print(My_list+[5,6,7])

# by * we can print multiple time list
print(My_list*3)


# add element by using insert

My_list = [1,2,3,4]
My_list.insert(2,5)
print(My_list)