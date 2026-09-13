"""
Function Assignment - Tommy Bough

This assignment will be focused on writing 3 functions that take input and return information."""

import random

# Defines a function, FtoC, that converts Farenheit to Celsius.
def FtoC(n: int) -> int:
    Celsius = (n - 32) / 1.8
    return(Celsius)

# Prints the result when given an integer value.
print(FtoC(100))

# Defines the function, BMI Formula, as a set of 2 integers.
def bmi_formula(w: int, h: int) -> int:
# Calculates BMI Result from w, weight in pounds, and h, height in inches.
    bmi_result = ((w / (h * h)) * 703)
    return(bmi_result)

# Prints the BMI Formula function.
print(bmi_formula(190, 70))

# Defines a function of elements.
def elements():
# Sets a list of 5 elements to choose at random from.
    set =('Carbon', 'Oxygen', 'Platinum', 'Neon', 'Radium')
    return random.choice(list(set))

print(elements())