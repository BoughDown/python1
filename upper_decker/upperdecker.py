"""
The Upper Decker - Tommy Bough

The objective is to create a program that reads a file, removes all the spaces, and saves it.
"""

# 'W' Means write mode, while 'r' means read.
with open('sample.txt', 'r') as stream:
    text = stream.read()
    print(text)
# Creates a for loop for the sample text file to replace space characters with characters with no space.
    # for char in stream.read():
    no_space = ""
        # if char == " ":
    new_text = text.replace(" ", no_space)

print(new_text)

with open('sample.txt', 'w') as stream:
    print(stream.write(new_text))

# test = "This is a rtsd string or whatever."

# result = "" 

# for char in test:
#     if char != " ":
#         result += char

# print(result)