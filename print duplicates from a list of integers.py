def repeat(list):
    size = len(list)
    repeated = []
    for i in range(size):
        k = i+1
        for j in range(k,size):
            if (list[i] == list[j] and list[i] not in repeated):
                repeated.append(list[i])
    return repeated
list = [10,20,30,20,20,30,40,50,-20,60,60,-20,-20]
print(repeat(list))
