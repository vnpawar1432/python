def table(n):
    for i in range(1,11):
        yield n*i
        i = i+1
print()
print("print table using generator object")

t = table(15)
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())

print()
print("print table using loop")

for a in table(15):
    print(a)