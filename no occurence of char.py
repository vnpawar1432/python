s = input("String: ")
s1 = {}
for i in s:
    if i in s1:
        s1[i] +=1
    else:
        s1[i] = 1
for i in s:
    if s1[i] !=0:
        print("{}{}".format(i,s1[i]),end="")
        s1[i]=0