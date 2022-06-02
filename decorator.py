# import functools
def my_decorator(func):
    # @functools.wraps(func)
    def wrapper():
        print("first line")
        func()
        print("3rd line")
    return wrapper

@my_decorator
def vaibhav():
    print("second line")

vaibhav()