"""
Password Generator - Tommy Bough

The goal is to import a large list of words and randomize them to create useable passwords.
"""

# Imports libraries needed.
import random
import os

# Allows the program to be ran on different computers.
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'words_alpha.txt')

# Creates lists for both large words and small words.
bigwords = []
smallwords = []

# Imports the file into VS Code
with open(file_path, 'r') as word_file:
    bigtext = word_file.readlines()

    # Puts words in either list depending on their size.
    for line in word_file:
        if len(line) >= 4:
            bigwords.append(line)
        elif len(line) <= 3:
            smallwords.append(line)

# Strips bigwords for the newline commands after each word.
bigwords = [line.strip() for line in bigtext]

# Selects 4 random words from the list.
word1 = (random.choice(bigwords))

word2 = (random.choice(bigwords))

word3 = (random.choice(bigwords))

word4 = (random.choice(bigwords))

# Prints each word to they could potentially be used.
print(f'Your password could be: {word1} {word2} {word3} {word4}')
