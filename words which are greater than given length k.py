# words which are greater than given length k

str = input("enter the string: ")
n = int(input())
li = str.split(" ")
for i in li:
    if(len(i)>n):
        print(i,end=" ")