# Print the 4 digit binary numbers that are divisible by 5

items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    print(x)
    if not x%5:
        items.append(p)
print(','.join(items))