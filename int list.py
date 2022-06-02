s = input()
li = s.split(" ")
l1 = []
for i in li:
    if i.isdigit():
      l1.append(i)
print(l1)
print(li)
print(l1[-2])