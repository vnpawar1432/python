list = [1, 2, 3, 4, 5, 6]


# List Comprehension

a = [x ** 3 for x in list]
print(a)

# Generator expression

z = (x ** 3 for x in list)

print(z)

print(next(z))

print(next(z))

print(next(z))

print(next(z))