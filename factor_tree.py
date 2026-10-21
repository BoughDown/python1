"""
Factor Tree - Tommy Bough

Create a factor tree for any given number.
"""

# Imports the time function to run a time decorator.
from time import time

# Created time decorator function.
def timed_function(original_function):
	def new_function(*args, **kwargs):
		starttime = time()
		result = original_function(*args, **kwargs)
		endtime = time()
		elapsedtime = endtime - starttime
		print(f'Program took {elapsedtime} to run.')	
		return result

	return new_function

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

# Determines if a number divides evenly into another.
def a_divides_into_b(a, b):
	if b % a == 0:
		return True
	else: return False

# Prints the factoring result.
def print_factor_tree(n: int):
	product = factoring(n)
	for factors in product:
		for i in range (1, 100000000000000000000000):
			factors.print(i)

	print(f'The factors of {n} include 2^{factors.count(2)}, 3^{factors.count(3)}, 5^{factors.count(5)}, 7^{factors.count(7)}, 11^{factors.count(11)}, 13^{factors.count(13)}')

# Printed factors wrapped in the time decorator.
timed_function(print_factor_tree(9473464))