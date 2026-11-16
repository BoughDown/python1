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

answer = tk.Label(base, text = "Answer will appear here")
answer.grid(row = 5, column = 4)

def calculate():
    """
    Gives the button a calculate function to command it.
    """
    if sign == '+':
        result = entry.getint + entry2.getint
        answer.configure(text = result)
        print(result)
    if sign == '-':
        result = entry.getint - entry2.getint
        answer.configure(text = result)
    if sign == 'x':
        result = entry.getint * entry2.getint
        answer.configure(text = result)
    if sign == '÷':
        result = entry.getint / entry2.getint
        answer.configure(text = result)
    

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
    sign.configure(text = 'x')

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

base.mainloop()