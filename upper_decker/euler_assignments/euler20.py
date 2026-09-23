def factorial(n: int) -> int:
    """
    Returns the factorial of a given number.
    
    Arguments:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the provided number.
    """
    # factorial is undefined for n < 0.
    if n < 0:
        raise ValueError("Factorial can only be computed for numbers >/= 0.")

    result = 1
    while n > 1:
        print(f"n is {n}")
        result = result * n
        print(f"result so far is {result}")
        n -= 1

# The pass command can be used to ignore functions without receiving an error.

factorial(8)