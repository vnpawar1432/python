def fib(limit):
    # Initialize first two
    a, b = 0, 1

    # One by one yield next  Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(x.__next__())  # In Python 3, __next__()
print(x.__next__())
print(x.__next__())
print(x.__next__())
# print(x.__next__())

# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)