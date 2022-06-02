# Python program to interchange first and last element
#      in list

# def Swaplist(Newlist):
#     Size = len(Newlist)
#
#     temp = Newlist[0]
#     Newlist[0] = Newlist[Size - 1]
#     Newlist[Size - 1] = temp
#     return Newlist
#
# Newlist = [12,15,18,21,24]
# print(Swaplist(Newlist))

Newlist = [11,12,13,14,15]

size = len(Newlist)
temp = Newlist[0]
Newlist[0] = Newlist[size - 1]
Newlist[size - 1] = temp
print(Newlist)
