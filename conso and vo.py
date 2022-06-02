s = input()
a = "aiuoe"
v =0
c = 0
for i in s:
    if(i=="a" or i=="u" or i=="e" or i=="o" or i=="i"):
       v+=1
    else:
        c+=1
if(v>0 and c>0):
    print("not homo")
elif(v==0 or c>0):
    print("homo")
elif(v>1 or c==0):
    print("homo")
# else:
#     print("not homo")