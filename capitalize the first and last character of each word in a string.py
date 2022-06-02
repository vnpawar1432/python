# capitalize the first and last character of each word in a string

str = "vaibhav pawar patil"
str1 = ' '.join(map(lambda str: str[:-1]+str[-1].upper(),str.title().split()))
print(str1)