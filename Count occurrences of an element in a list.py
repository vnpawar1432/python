# Count occurrences of an element in a list

list = [1,2,3,3,2,1]
a = 2
count = 0
for i in list:
    if(i==a):
        count = count+1
print(count)
