"""
Question & Answer Assignment - Tommy Bough

The goal is to create an input function by having program ask the user a question. 
"""

# Asks the user how dogs the user has, as well as storing the variable as 'user_dogs'.
user_dog = input("How many dogs do you have?\n")

# This forces the user input value of the number of dogs to be an integer instead of a string.
user_dog = int(user_dog)

# This command evaluates the number of dog ears by multiplying the number of dogs by 2.
print(f"So you have {2*user_dog} dog ears.")