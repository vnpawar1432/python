d = {"a":{"name":"vaibhav","surname":"pawar"},"b":{"name":"samruddhi","surname":"Bhandarkar"}}
for i in d:
    print(i)
for i in d.keys():
    print(i)
print()
print("-----------------")
print()
for x in d:
    print(d[x])
for x in d.values():
    print(x)
print()
print("-----------------")
print()

for a in d.items():
    print(a)

for a,b in d.items():
    print(a,b)
