"""
Time Flies - Tommy Bough

This assignment will attempt to accurately generate a random number representing seconds, as well as showing that number as a form of minutes and hours.
"""

# Imports random numbers into this python document.
from random import randint

# Sets seconds as a random integer between 100 and 8000, as the parameters dictate.
seconds = randint(100, 8000)
# Sets remainder_seconds as the amount of seconds that could not divide into 60.
remainder_seconds = (seconds%60)

# Sets whole_minutes as the amount of minutes that can be divided by 60 evenly.
whole_minutes = (seconds//60)
# Sets remainder_minutes as the remainder of minutes that could not be divided by 60 evenly.
remainder_minutes = (whole_minutes%60)

# Sets whole_hours as the amount of whole minutes that could be divided by 60 evenly.
whole_hours = (whole_minutes//60)
remainder_hours = (whole_hours%24)

whole_days = (whole_hours//24)
remainder_days = (whole_hours%24)

whole_years = (whole_days//365)

# The following commands were to ensure the code was operating properly.
# print(seconds)
# print(remainder_seconds)
# print(whole_minutes)
# print(remainder_minutes)
# print(whole_hours)

if whole_hours == 0:
    print(f"{seconds} is {whole_minutes} minutes, and {remainder_seconds} seconds")

if 0 < whole_hours < 2:
    print(f"{seconds} is {whole_hours} hour, {remainder_minutes} minutes, and {remainder_seconds} seconds")

if 1 < whole_hours < 24:
    print(f"{seconds} is {whole_hours} hours, {remainder_minutes} minutes, and {remainder_seconds} seconds")

if whole_hours > 24:
    print(f"{seconds} seconds is {whole_days} days, {remainder_hours} hours, {remainder_minutes} minutes, and {remainder_seconds} seconds")

if whole_years > 0:
    print(f"{seconds} seconds is {whole_years} years, {remainder_days} days, {remainder_hours} hours, {remainder_minutes} minutes, and {remainder_seconds} seconds")