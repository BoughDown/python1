"""
Euler Number 9

Find a pythagorean triple with a + b + c = 1000
"""

from math import sqrt

def is_pythagorean_triple(a, b, c):
    pass

def find_c(a:int, b:int) -> int:
    c = sqrt(a ** 2 + b ** 2)
    if c == int(c):
        return int(c)
    else:
        # return -1
        error = f"{a} and {b} do not compute to a perfect pythagorean triple."
        raise ValueError(error)

# print(find_c(3, 4))

with open("log.txt", "w") as file_stream:
    for i in range(1, 1001):
        for j in range(1, 1001):
            try:
                c = find_c(i, j)
                sum = i + j + c
                a = i
                b = j
                if sum == 1000:
                    print(f"{a}, {b}, and {find_c(i, j)} is a pythagorean triple")
                    
            except ValueError as e:
                    print(e, file=file_stream)