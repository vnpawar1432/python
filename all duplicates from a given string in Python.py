# all duplicates from a given string in Python
str = "vaibhav"
s = set(str)
s= "".join(s)
print("without order:: ",s)
# with order
t=""
for i in str:
    if(i in t):
        pass
    else:
        t=t+i
print("with order: ",t)