def list(li):
    li.append(5)
    li.append(6)
    print("list inside func ",li)
li = [1,2,3,4]
list(li)
print("list outside func ",li)