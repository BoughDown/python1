"""
Final Project GUI - Tommy Bough

Create a GUI for the user to interact with.
"""

import tkinter as tk
import requests
from class_gui import APIInterface


gui = tk.Tk()

gui.title("Weather Finder")
gui.geometry("1200x800")

background_image = tk.PhotoImage(file = "final_project\\background_image_2.gif")
background_label = tk.Label(gui, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

interface = APIInterface(gui)

gui.mainloop()