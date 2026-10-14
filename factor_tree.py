"""
Factor Tree - Tommy Bough

Create a factor tree for any given number.
"""

from time import time

time()



def factoring(n, factors = []):
	"""
	Returns the factors for a given number, n.

	Arguments:
		n (int): The number that factors are solved for.

	Keyword Arguments:
		i (int): The factors that are solved. 
	"""
	if n <= 0:
			raise ValueError("There are infinitely many factors of zero.")
		
	if n == 1:
		return factors
	
	for i in range(2, n + 1):
		if a_divides_into_b(i, n):
			factors.append(i)
			return factoring(n//i, factors)


def a_divides_into_b(a, b):
	if b % a == 0:
		return True
	else: return False

def print_factor_tree(n: int):
	product = factoring(n)
	for factors in factors:
		for i in range (1, 100000000000000000000000):
			factors.count(i)

	print(f'The factors of {n} include 2^{factors.count(2)}, 3^{factors.count(3)}, 5^{factors.count(5)}, 7^{factors.count(7)}, 11^{factors.count(11)}, 13^{factors.count(13)}')

print_factor_tree(9473464)

# factors.sort()

# print(factors)

