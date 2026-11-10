import tkinter as tk

window = tk.Tk()

window.title("Testing")
window.geometry("600x500")

text_label = tk.Label(window, text = "Something")
text_label.pack()

entry_label = tk.Entry(window)
entry_label.pack()

# def say_hi():
#     print("Hi")
#     text_label.configure(text = "Hi")
#     button.pack_forget()

def button_action():
    """
    Get the input from the entry label and output it in a text label.
    """
    user_input = entry_label.get()
    print(user_input)
    result_label.configure(text = user_input)

button = tk.Button(window, 
                         text = "Do Not Press", 
                         bg = "#FF0000", 
                         fg = "#FCFCFC", 
                         command = button_action
                        )
button.pack()

result_label = tk.Label(window, text = "")
result_label.pack()

window.mainloop()