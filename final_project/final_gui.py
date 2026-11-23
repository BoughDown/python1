"""
Final Project GUI - Tommy Bough

Create a GUI for the user to interact with.
"""

import tkinter as tk

gui = tk.Tk()

gui.title("Weather Finder")
gui.geometry("1200x800")

background_image = tk.PhotoImage(file = "final_project\\background_image_2.gif")
background_label = tk.Label(gui, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

longitude_label = tk.Label(gui, 
                           text = "Longitude", 
                           font = ("Times New Roman", 12, "bold"))
longitude_label.place(x = 300, y = 200)

longitude_entry = tk.Entry(gui)
longitude_entry.place(x = 270, y = 230)

latitude_label = tk.Label(gui, 
                          text = "Latitude", 
                          font = ("Times New Roman", 12, "bold"))
latitude_label.place(x = 800, y = 200)

error = tk.Label(gui, 
                 fg = '#990000',
                 font = ('Times New Roman', 12, 'Bold'))

latitude_entry = tk.Entry(gui)
latitude_entry.place(x = 770, y = 230)

results = tk.Label(gui, 
                   text = "Weather Results", 
                   font = ("Times New Roman", 12, "bold"))
results.place(x = 530, y = 300)

temperature = tk.Label(gui, 
                       text = "Temperature")
temperature.place(x = 530, y = 330)

rainfall = tk.Label(gui, 
                    text = "Rainfall")
rainfall.place(x = 530, y = 360)

snowfall = tk.Label(gui, 
                    text = "Snowfall")
snowfall.place(x = 530, y = 390)

wind_speed = tk.Label(gui, 
                      text = "Wind Speed")
wind_speed.place(x = 530, y = 420)

wind_direction = tk.Label(gui, 
                          text = "Wind Direction")
wind_direction.place(x = 530, y = 450)

calculate = tk.Button(gui,
                    text = "Calculate", 
                    background = "#990000",
                    fg = '#FFFFFF')
calculate.place(x = 550, y = 230)

gui.mainloop()