"""
Utilities for Euler Problems

Euler Problems are a list of coding objectives you can complete for fun.
"""

# White board notes
# Attributes keep track of numbers. May need number integers, storing numbers as strings. 
# Methods are ways in which you compute programs. May need factorial, reversing, palindrome, summing digits together.

class EulerNumber:
    """
    EulerNumber is a helper class for solving Euler Problems from the Euler Archive.
    
    Attributes:
        number (int): The actual number.
        number_as_str (str): The number as a string.

    Methods:
        factorial
        reverse
        palindrome
        sum_of_digits
    """

    # Self is very important to have here. Init stands for initialize. the "__" on either side means you ask python to call this program.
    def __init__(self, number: int):
        # TODO makes sure that the number is actually an integer.
        self.number = number
        self.number_as_str = str(number)

    def reverse(self) -> int:
        """
        Return a reversed integer version of the Euler Number.

        Returns:
            int: The reversed number.
        """

        # Used string slicing to reverse the string.
        reversed = self.number_as_str[::-1]
        reversed_as_int = int(reversed)
        return reversed_as_int

    def palindrome(self) -> bool:
        """
        Returns a boolean indicating if the number is a palindrome.

        Returns:
            bool: Is the number a palindrome.
        """

        difference = self.number - self.reverse()
        if difference == 0:
            return True
        else: 
            return False

if __name__ == "__main__":
    euler_test = EulerNumber(151)
    print(euler_test.palindrome())

    for i in range(10, 1000):
        test = EulerNumber(i)
        if test.palindrome():
            print(test.number)