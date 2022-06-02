a = input("enter the number as input:  ")
b = a.split(", ")
b = [int(i) for i in b]
b.sort()
print(b[-2])
