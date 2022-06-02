# remove digit from string

str = "vaibhav 21 pawar 97"
# res = ''.join([i for i in str if not i.isdigit()])
# print(res)
count = 0
for i in str:
    if(i.isdigit()):
        count = count+1
        str = str.replace(i,"")
print(str,count)