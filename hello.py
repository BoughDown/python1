"""
This is some code to get students started.

A longer description of the file will appear here.
"""
# This is a one line comment. The format above is a docstring.

# This is importing just the "randint" function. This is fine.
from random import randint
# randint

# This is importing the random module. This is fine.
# import random 
# random.randint

# Never do the following.
# from random import *

user_input = input("How many dogs do you have?\n")

user_input_as_int = int(user_input)

print(f"So you have {user_input_as_int * 4} dog legs")

print(randint(1,6))

# This prints out "hello world". 
print("hello world") # This is a trailing comment. Do not use in the classroom.