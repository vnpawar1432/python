help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

# initializing string
test_str = "zero four zero eight"

# printing original string
print("The original string is : " + test_str)

# Convert numeric words to numbers
# Using join() + split()
res = ''.join(help_dict[ele] for ele in test_str.split())

# printing result
print("The string after performing replace : " + res)