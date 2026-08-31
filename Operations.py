# operations worksheet written by Joe Manlove
# Used in Programming and Methodologies 1 in Python
# Last Revised 5/19/2020

# Instructions: You should write code below each comment attempting to carry out the instructions
# you should also include print statements about what you're doing so the output is readable.
# There's an example at the start of the Boolean Section
# I've included some print statements to keep sections straight, no need to change them.
# in cases where errors are generated, feel free to comment out your attempt, but please explain the error

# This section is for numerical operations
print('Numerical Operations Section')

# make two numerical values x and y, initialize them to 4 and 9 respectively
x = int(4)
y = int(9)

# Print out the types of x and y.
# print(str(x, y))
print(type(x), type(y))

# print x+y
print(x + y)

# print x/y
print(x/y)

# print the type of x/y
print(type(x/y))

# print x*y
print(x*y)

# print the type of x*y
print(type(x*y))

# print x + 0.0
print(x + int(0.0))

# print the type of x+0.0
print(type(x + 0.0))

# print x//y
print(x//y)

# print the type of x//y
print(type(x//y))

# write a comment explaining the difference between // and /.
# / Indicates division, for example 4/8 = 1/2. Meanwhile, // means dividing by the fraction. For example, 4//8 = 32.

# print x<y
print(x<y)

# why is (x<y) == True?
# x<y is true since 4 is less than 9, and that is what x and y are set equal to, respectively.

# Notice that == and = are different, perform some experimentation or googling to discover the difference
# print out a string explaining the difference
print("The equal sign in python, =, means to set something equal to another. For example, x = int(4). The double equal sign, ==, means to compare two values for equality.")

# print y%x
print(y%x)

# being confused by this one is ok. There'll be a deeper dive on this seperately.

# this is the Boolean Section
# a boolean is a variable that is either True or False
# notice that True and False are case sensative
print('Boolean Operations Section')

# make a variable t and a variable f, set them to True and False respectively
t = True
f = False

# print t and f 
print(f'{t} and {f}')

# I did this one for you, you're welcome :)
# notice and is a special word, don't try to use it as a variable name :P
print(f'{t} and {f} is: {t and f}')

# print t or f
print(f'{t} or {f}')

# print !t
# print(!t)
# ! Is its own command, meaning "not"
# print(f'!{t}')
print(not t)
# print(!f)
# There is invalid syntax for the operation above.

# print !f
print(not f)

# This is the String Section
print('String Operations Section')

# make two variables, s and ten set them to 'This is a string.' and '10' respectively.
s = 'This is a string'
ten = '10'

# print s + ten
print(s + ten)

# print s - ten
# print(s - ten)
# Cannot subtract two string values from each other


# print ten + s
print(ten + s)

# print the type of ten
print(type(ten))

# print ten.isnumeric()
print(ten.isnumeric)

# print len(ten) and len(s)
print(len(ten), 'and', (len(s)))
print(len(s))
print(len(ten))

# print a string explaining the results
print("(Len) prints how many characters are in a string value.")

# print s[:4]
print(s[:4])

# print s[:4]
print(s[:4])

# print s[0:4]
print(s[0:4])

# print s[2:]
print(s[2:])

# print s[-4:]
print(s[-4:])

# print s[0]
print(s[0])

# print a string that explains this [] thing...
print("The [] function operates on the characters in an operation. For example, s[0:4] shows the characters from 0 to 4 in the string value of s. A negative [] value shows the last characters. For example, s[-4:] shows the last 4 characters in the string.")

# This is the Mixed Type Section
print('Mixed Type Section')


# print x*ten
print(x*ten)

# print 2 * s
print(2*s)

# print t*y
print(f'{t}*{y} is {t*y}')

# print f*y
print(f'{f}*{y} is {f*y}')

# print the first 5 letters of s six times
print(s[:5]*6)

# print s + y or explain the issue
# print(s + y)
# The issue for the operation above, is that you cannot add string values to integer values and vice versa.

# print ten + y or explain the issue
# print(ten + y)
# The issue, once more, for the operation above, is that you cannot add string values to integer values and vice versa.

# force ten + y to work by turning both into strings
print(ten + str(y))

# force ten + y to work by turning both into numbers
print(int(ten) + y)
