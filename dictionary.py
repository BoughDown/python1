# lists are ordered and indexed by 0,1,2,3,4,..
test_list = [2, 3, 5, 7, 11, 13]

# make a dictionary
indi = {'name': 'Indi', 'age': 5, 'weight': 70, 1: 'puddles'}

print('Keys:')
# prints out the keys
for x in indi:
    print(x)

print('Values:')
# prints out the values
for x in indi.values():
    print(x)

# print out items
print('Items:')
for key, value in indi.items():
    print(key, value)

# looking things up
print(f"The phone number in the dict is: {indi.get('phone_number', 'Not found...')}")

if not indi.get('phone_number'):
    print("Indi doesn't have a phone number in the system...")


# adding to a dict
indi['color'] = 'Blue Merel'

print(indi)

# deleting items
print(indi.pop(1))
# this is not recommended
del indi['color']

print(indi)

# WARNING: COPY AND ALIAS ARE DIFFERENT!!!
# this is aliasing
# blue = indi
# this is copying
blue = indi.copy()
blue['name'] = 'Blue'
blue['weight'] = 28

print(blue)
print(indi)

# deletes all items
indi.clear()

print(indi)