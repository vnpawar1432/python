str1 = input("enter the string: ")
p = {}
for i in str1:
    if i in p:
        p[i] +=1
    else:
        p[i] = 1
for i in str1:
    if p[i] !=0:
        print("{}{}".format(i,p[i]),end="")
        p[i]=0


# d = min(p, key=p.get)
# z = max(p, key=p.get)
# print(z)
# print(d)

