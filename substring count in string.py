string = input("Enter the string: ")
sub_string = input("Enter sub string: ")
count = 0
for i in range(len(string)):
    if string[i:].startswith(sub_string):
        count += 1
print(count)