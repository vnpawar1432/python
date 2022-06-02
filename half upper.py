str =input("enter String: ")
mid = len(str)//2
res =""
for i in range(len(str)):
    if(i >= mid):
       res += str[i].upper()
    else:
        res += str[i]
print(res)