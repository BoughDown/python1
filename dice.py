"""
Dice Project - Tommy
"""

from random import randint

list_die = []

number = input("How many die would you like to roll?\n")

number_int = int(number)

sides = input("How many sides on each dice?\n")

sides_int = int(sides)

# print(randint(1, sides_int))

print("Results:")

for i in range(0, number_int):
    # print(f"{1, number_int}")
    list_die.append(randint(1, sides_int))

print(list_die)