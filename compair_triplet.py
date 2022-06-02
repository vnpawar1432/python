inp = 3
a = []
for i in range(0,inp):
    elem = int(input())
    a.append(elem)

inp = 3
b = []
for i in range(0,inp):
    elem = int(input())
    b.append(elem)
def compairTriplet(a,b):
    alice = bob = 0
    for j in range(3):
        if(a[j]>b[j]):
            alice+=1
        elif (a[j] < b[j]):
            bob+= 1
    return alice,bob

print(compairTriplet(a,b))