s = input()
p = input()
E = set({})
F = set({})
for i in s:
    if(i.isdigit()):
        E.add(i)
for j in p:
    if(i.isdigit()):
        F.add(i)
print(E.difference(F))