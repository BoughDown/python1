"""
Factor Tree - Tommy Bough

Create a factor tree for any given number.
"""

twos = []
threes = []
fives = []
sevens = []

def factoring(n):
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
		return n	
		
	if n == 2:
		twos.append(2) 
		return n
	
	if n % 2 == 0:
		new_factor = n / 2
		twos.append(2)
		factoring(new_factor)

	if n % 3 == 0:
		new_factor = n / 3
		threes.append(3)
		factoring(new_factor)

	if n % 5 == 0:
		new_factor = n / 5
		fives.append(5)
		factoring(new_factor)

	if n % 7 == 0:
		new_factor = n / 7
		sevens.append(7)
		factoring(new_factor)

	new_factor = n

factoring(20)

n = int

print(8%5)
print(f"{20} has factors: 2^{twos.count}, 3^{threes.count}, 5^{fives.count}, 7^{sevens.count}.")