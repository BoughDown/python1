"""
Dictionary Assignment - Tommy Bough

Create a dictionary and perform various actions on said dictionary.
"""

# Creating the dictionary of a dog named Walter.
walter = {'Name': 'Walter', 'Age': 4, 'Weight': 20}

# Adding the value, color, to the dictionary, and setting they key as 'black'.
walter['Color'] = 'Black'

# Printing updated dictionary.
print(walter)

# Removes the value, name, from the dictionary as well as the corresponding key.
print(walter.pop('Name'))

# Prints the updated dictionary with no name value.
print(walter)

# Updates Walter's age as 3.5 instead of 4.
walter['Age'] = 3.5

# Prints dictionary with new age updated.
print(walter)