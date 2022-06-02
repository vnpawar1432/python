# check whether the string is Symmetrical or Palindrome
# s1 = "mom"
# s2 = s1[::-1]
# if(s1==s2):
#     print("string is palindrom")
# else:
#     print("string is not palindrom")
#
str = "mommomm"
half = int(len(str)/2)

if len(str)%2 == 0:
    str1 = str[:half]
    str2 = str[half:]
else:
    str1 = str[:half]
    str2 = str[half+1:]

if (str1==str2):
    print("string is symetrical")
else:
    print("string is not symetrical")

if(str1==str2[::-1]):
    print("string is palindrom")
else:
    print("string is not palindrom")