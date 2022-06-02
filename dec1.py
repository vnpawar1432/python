def my_decorator(f):
    def my_method():
        print("Hi")
        f()
        print("you are looking very good today")
    return my_method

@my_decorator
def show():
    print("Vaibhav")

show()