def add_num_decorator(f):
    def add_num_wrapper(i,j):
        print(j-i)
        f(i,j)
        print(i*j)
    return add_num_wrapper

@add_num_decorator
def add(i,j):
    print(i+j)

add(10,20)
