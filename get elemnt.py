d = {"a":"apple","b":"ball","c":"cat"}
for i in d:
    print(i)
    print(d[i])
# if we just take i it will print only keys
# if we take (dict name +i) d[i] it will print values

d = {"a":"apple","b":"ball","c":"cat"}
for a in d.items():
    print(a)
# if we declare d.items() range it will print items dictionary

d = {"a":"apple","b":"ball","c":"cat"}
for a in d.keys():
    print(a)

d = {"a":"apple","b":"ball","c":"cat"}
for a in d.values():
    print(a)

d = {"a":"apple","b":"ball","c":"cat"}
for x,y in d.items():
    print(x,y)

