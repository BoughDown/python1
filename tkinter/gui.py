"""
Make A GUI Assignment - Tommy Bough

Make an interactive GUI with a label, an image, 2 buttons that do something, and a text entry box.
"""

import tkinter as tk

base = tk.Tk()

base.title("Calculator")
base.geometry("500x500")

question = tk.Label(base, text = "Number 1")
question.grid(row = 0, column = 0)

question2 = tk.Label(base, text = "Number 2")
question2.grid(row = 0, column = 7)

entry = tk.Entry(base)
entry.grid(row = 1, column = 0)

entry2 = tk.Entry(base)
entry2.grid(row = 1, column = 7)

sign = tk.Label(base, text = "Enter an Operation")
sign.grid(row = 1, column = 4)

answer = tk.Label(base, text = "")
answer.grid(row = 5, column = 4)

def calculate():
    """
    Gives the button a calculate function to command it.
    """
    if sign.getvar == '+':
        result = int(f'{entry.getint + entry2.getint}')
        answer.configure(text = f'{result}')

def plus_operation():
    """
    Adds the operations and numbers to the text label.
    """
    sign.configure(text = '+')

def minus_operation():
    """
    Adds the operations and numbers to the text label.
    """
    sign.configure(text = '-')

def multiply_operation():
    """
    Adds the operations and numbers to the text label.
    """
    sign.configure(text = '-')

def division_operation():
    """
    Adds the operations and numbers to the text label.
    """
    sign.configure(text = '÷')

plus = tk.Button(base, text = "+", bg = "#A0BEBD", fg = "#000000", command = plus_operation)
plus.grid(row = 2, column = 2)

minus = tk.Button(base, text = "-", bg = "#A0BEBD", fg = "#000000", command = minus_operation)
minus.grid(row = 2, column = 3)

multiply = tk.Button(base, text = "x", bg = "#A0BEBD", fg = "#000000", command = multiply_operation)
multiply.grid(row = 2, column = 5)

divide = tk.Button(base, text = "÷", bg = "#A0BEBD", fg = "#000000", command = division_operation)
divide.grid(row = 2, column = 6)

equals = tk.Button(base, text = "=", bg = "#A0BEBD", fg = "#000000", command = calculate())
equals.grid(row = 4, column = 4)

# decimal = tk.Button(base, text = ".", bg = "#A0BEBD", fg = "#000000", command = calculate)
# decimal.grid(row = 6, column = 2)

# one = tk.Button(base, text = "1", bg = "#A0BEBD", fg = "#000000", command = calculate)
# one.grid(row = 3, column = 1)

# two = tk.Button(base, text = "2", bg = "#A0BEBD", fg = "#000000", command = calculate)
# two.grid(row = 3, column = 2)

# three = tk.Button(base, text = "3", bg = "#A0BEBD", fg = "#000000", command = calculate)
# three.grid(row = 3, column = 3)

# four = tk.Button(base, text = "4", bg = "#A0BEBD", fg = "#000000", command = calculate)
# four.grid(row = 4, column = 1)

# five = tk.Button(base, text = "5", bg = "#A0BEBD", fg = "#000000", command = calculate)
# five.grid(row = 4, column = 2)

# six = tk.Button(base, text = "6", bg = "#A0BEBD", fg = "#000000", command = calculate)
# six.grid(row = 4, column = 3)

# seven = tk.Button(base, text = "7", bg = "#A0BEBD", fg = "#000000", command = calculate)
# seven.grid(row = 5, column = 1)

# eight = tk.Button(base, text = "8", bg = "#A0BEBD", fg = "#000000", command = calculate)
# eight.grid(row = 5, column = 2)

# nine = tk.Button(base, text = "9", bg = "#A0BEBD", fg = "#000000", command = calculate)
# nine.grid(row = 5, column = 3)

# zero = tk.Button(base, text = "0", bg = "#A0BEBD", fg = "#000000", command = calculate)
# zero.grid(row = 6, column = 1)

base.mainloop()