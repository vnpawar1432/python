# count Even and Odd numbers in a List
list = [78,65,42,36,15,2,8,4,89,8,65]
even = 0
odd = 0
for i in list:
    if(i%2==0):
        even += 1
    else:
        odd += 1
print(even)
print(odd)