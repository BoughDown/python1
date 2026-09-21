"""
The Upper Decker - Tommy Bough

The objective is to create a program that reads a file, removes all the spaces, and saves it.
"""

# 'W' Means write mode, while 'r' means read.
with open('sample.txt', 'r') as stream:
    print(stream.read())

# Creates a for loop for the sample text file to replace space characters with characters with no space.
for char in stream.read():
    no_space = ""
    if char in " ":
        stream.read().replace(char, no_space)