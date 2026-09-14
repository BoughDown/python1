"""
Looper Assignment - Tommy Bough

Goal is to create a program that contains at least 2 loops.
"""

# Creates an input for a user to type a phrase. AV meaning anti-vowel.
av_input = input("Type Phrase Here\n")

# Creates a vowel list and sets each vowel as a string in the list.
vowels = []
vowels = ["a", "e", "i", "o", "u"]

# Makes the user input all lowercase so the list is simpler to go through.
av_lower = av_input.lower()

result = ""

# For loop so the lowercase input can filter out the vowels and remove them.
for i in av_lower:
    if i in vowels:
        i == ""
        result += ""
    else:
        result += i

# Prints out the input, with vowels now filtered out.
print(result)

# Creates a list of perfect square roots up to 20.
perfect_square_roots = []
perfect_square_roots = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Creates a for loop to square each value in the list, find the last digit in each string, and see if its an even or odd number.
for i in (perfect_square_roots):
    perfect_square = str(i * i)
    if perfect_square[-1:] in ("0", "2", "4", "6", "8"):
        print("Even Perfect Square!")
    if perfect_square[-1:] in ("1", "3", "5", "7", "9"):
        print("Odd Perfect Square!")