def collatz(n, i = 1):
    """
    Returns the length of a collatz sequence for a provided number.

    Arguments:
        n (int) = The number you begin with and want to calculate the conjecture for.

    Keyword Arguments:
        i (int): The index in the collatz sequence. 
    """
    # print(n)
    if n <= 0:
        raise ValueError("The Collatz sequence is not defined for negative values and zero.")

    if n == 1:
        return i
    
    # If even n%2 == 0
    odd = n % 2
    if odd:
        new_number = 3 * n + 1
    else: 
        new_number = n//2

    i += 1
    return collatz(new_number, i)

n_max_length = 0
max_length = 0
for i in range(1, 1000001):
    length = collatz(i)
    if length > max_length:
        n_max_length = i
        max_length = length
        print(f"New max: {i} has a Collatz Sequence of length {length}.")