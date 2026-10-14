from time import time
from euler_assignments import euler20
# import factorial

def timed_function(original_function):
    def new_function(*args, **kwargs):
        start_time = time()
        print(f"Starting at {start_time} seconds.")
        result = original_function(*args, **kwargs)
        end_time = time()
        print(f"Ending at {end_time} seconds.")
        elapsed_time = end_time - start_time
        print(f"Run time of {elapsed_time} seconds.")
        return result

    return new_function

def verbose(original_function: function):
    def verbose_function(*args, **kwargs):
        print(f'Calling {original_function.__name__} on {args} and {kwargs}.')
        result = original_function(*args, **kwargs)
        print(f'Returning {result}.')
        return result

    return verbose_function

def logger(original_function: function):
    def logged_function(*args, **kwargs):
        with open("log.txt", 'a') as log_file:
            print(f'Calling {original_function.__name__} on {args} and {kwargs}.', file = log_file)
            result = original_function(*args, **kwargs)
            print(f'Returning {result}.', file = log_file)
        return result

    return logged_function

@logger
@timed_function
@verbose
def example(a: int, b: float, c: int, d = 0, e = 4, f = 6):
    return a + b + c - d * e * f

example(1, 2, 3, d = 2, e = 1)