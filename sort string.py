n = int(input())
for j in range(n):
    str = input()
    li = []
    for i in str:
        li.append(i)
    li.sort()
    str1 = "".join(li)
print(li)