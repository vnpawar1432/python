def add():
    for i in range(5):
        if(i%2==0):
            yield i


a = add() # object
print(a.__next__())  #iterator
print(a.__next__())  #iterator
print(a.__next__())  #iterator

# for a in add():
#     print(a)