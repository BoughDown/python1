# Will need numbers from 100 to 999.
# Will need more numbers from 100 to 999.
# Calculate the product of the two numbers.
# CHeck if the numbers calculate to become a palindrome.
# Find the largest palindrome calculated from our selected three digit numbers.

from time import time
start = time()

# palindromes = []
biggest_palindrome_so_far = 0
factors_of_biggest_so_far = [0,0]

for i in range(100,1000):
    for j in range(100,1000):
        if j > i:
            break
        product = i*j
        product_string = str(product)
        product_string_reversed = product_string[::-1]
        product_reversed = int(product_string_reversed)
        if product == product_reversed:
            if product > biggest_palindrome_so_far:
                biggest_palindrome_so_far = product
                factors_of_biggest_so_far = [i,j]
            # print(f'{i} * {j} = {product}')
            # palindromes.append(product)

end = time()

i = factors_of_biggest_so_far[0]
j = factors_of_biggest_so_far[1]

# print(max(palindromes))
print(f"The biggest palindrome is {biggest_palindrome_so_far} = {i} * {j}")
print(end-start)