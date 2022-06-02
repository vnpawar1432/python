import sys
a=sys.stdin.readline()
b = {}
for i in a.split():
    if i in b:
              b[i]+=1
    else:
         b[i]=1
max=max(b,key=b.get)
print("maximum Frequency :"+max)
