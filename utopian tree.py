n = int(input())
h=1
for i in range(n+1):
    if(i ==0):
        h = h
        # print(h)
    elif(i%2 != 0):
        h = h*2
        # print(h)
    elif(i%2==0):
        h = h+1
        # print(h)
print(h)