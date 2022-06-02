s = "vaibhav"
l = len(s)
mid = l/2
s1 =''
for i in range(l):
    if(i>mid):
        s1 += s[i].upper()
    else:
        s1 += s[i]
print(s1)