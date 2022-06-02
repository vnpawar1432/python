d = {"a":{"name":"vaibhav","surname":"pawar"},"b":{"name":"samruddhi","surname":"Bhandarkar"}}
print(d)
print("nested dictionary")
print("---------------------")
print()


d["a"]["name"] = "vinayak"
d["b"]["name"] = "vaibhav"
d["b"]["surname"] = "Pawar"
print(d)
print("modified value of dictionary")
print("----------------------")

d["a"]["age"] = 27
d["b"]["age"] = 25

print(d)
print("adding value in nested dictionary")
print("----------------------")

del d["a"]["age"]
del d["b"]["age"]

print(d)
print("delete value from nested dictionary")
print("----------------------")


