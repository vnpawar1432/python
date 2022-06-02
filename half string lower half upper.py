str = input("String: ")
half = int(len(str)/2)

if len(str)%2 == 0:
    str1 = str[:half]
    str2 = str[half:]
else:
    str1 = str[:half]
    str2 = str[half+1:]

if (str1==str2):
    print("symmetrical")
else:
    print("not symmetrical ")

