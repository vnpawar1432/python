# Swap commas and dots in a String
str = "12,13.14"
str = str.replace(",","9")
str = str.replace(".",",")
str = str.replace("9",".")
print(str)