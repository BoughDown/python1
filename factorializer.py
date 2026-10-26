"""
Factorializer - Tommy Bough

The goal is to create an integer based function based on prior code.
"""

def factorial(n: int):
    """
    Returns the factorial of a non-negative integer. Note, 0! = 1.

    Args:
        n (int): The non-negative integer to calculate the factorial of.
    """

    # check if n can be treated as an integer
    # in the video I used "type(n) != int"
    # isinstance is a bit safer as it allows for object inheritance
    if not isinstance(n, int):
        raise TypeError("Not of integer type, n must be a positive integer.")
    if n < 0:
        raise ValueError("n must be a positive integer.")

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def input_integer(prompt: str= 'Please, input an integer.\n'):
    """
    Read a string from standard input. The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a trailing newline before reading input.
    Input is cast to an integer and returned, non-integer inputs raise TypeErrors.

    Keyword Arguments:
        prompt (str): The prompt string printed into the console.
    """
    # Sets a variable as the input
    user_input = input(prompt)

    # Changes user_input into an integer if possible.
    try:
        number = int(user_input)
        print(f'You said {number}. This is of type: {type(number)}')

    # Raises error if input is not a number.
    except TypeError:
        print('That is not a number.')

    # Raises error if input is not an integer but is a number.
    except ValueError:
        print('That is not an integer.')

    # Raises error if user quits terminal during process.
    except BaseException as error:
        print('Maybe next time...')
        raise error

    # Runs factorial on user input if user_input is an integer.
    else:
        print(factorial(number))

    # Always runs this command to show it does work.
    finally:
        print('Function Complete')

input_integer()