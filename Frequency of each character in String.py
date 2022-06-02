# Frequency of each character in String
str1 = "vaibhav"
all_frq = {}
for i in str1:
    if i in all_frq:
        all_frq[i] +=1
    else:
        all_frq[i] = 1
# a = ', '.join(all_frq)
# min frequency char
res = min(all_frq, key = all_frq.get)

# min frequency char
res1 = max(all_frq, key = all_frq.get)

print(all_frq)
print(res)
print(res1)