"""
Final Project Class - Tommy Bough

Document that creates a viable class so the project is more portable.
"""

import tkinter as tk

class APIInterface:
    """
    Provides entry boxes and labels that directs the user to input latitudes and longitudes as well as a calculation function to convert latitudes and longitudes into weather results.
    
    Parameters:
        Gui: Tkinter object
    """

    def __init__(self, gui):

        self.latitude_value = tk.StringVar()

        self.longitude_value = tk.StringVar()

        self.longitude_label = tk.Label(gui, 
                           text = "Longitude", 
                           font = ("Times New Roman", 12, "bold"))
        self.longitude_label.place(x = 300, y = 200)

        self.longitude_entry = tk.Entry(gui,
                                        textvariable = self.longitude_value)
        self.longitude_entry.place(x = 270, y = 230)

        self.latitude_label = tk.Label(gui, 
                                text = "Latitude", 
                                font = ("Times New Roman", 12, "bold"))
        self.latitude_label.place(x = 800, y = 200)

        self.latitude_entry = tk.Entry(gui,
                                       textvariable = self.latitude_value)
        self.latitude_entry.place(x = 770, y = 230)

        self.error = tk.Label(gui, 
                 text = 'Error: Invalid Entry',
                 bg = '#000000',
                 fg = '#990000',
                 font = ('Times New Roman', 15, 'bold'))

        self.results = tk.Label(gui, 
                        text = "Weather Results", 
                        font = ("Times New Roman", 12, "bold"))
        self.results.place(x = 530, y = 300)

        self.temperature = tk.Label(gui, 
                                   text = "Temperature")
        self.temperature.place(x = 530, y = 330)

        self.rainfall = tk.Label(gui, 
                                text = "Rainfall")
        self.rainfall.place(x = 530, y = 360)

        self.snowfall = tk.Label(gui, 
                                text = "Snowfall")
        self.snowfall.place(x = 530, y = 390)

        self.wind_speed = tk.Label(gui, 
                                  text = "Wind Speed")
        self.wind_speed.place(x = 530, y = 420)

        self.wind_direction = tk.Label(gui, 
                                      text = "Wind Direction")
        self.wind_direction.place(x = 530, y = 450)

        self.calculate = tk.Button(gui,
                            text = "Calculate", 
                            background = "#990000",
                            fg = '#FFFFFF')
        self.calculate.place(x = 550, y = 230)

    def calculation(self):
        """
        Sends the latitude and longitude into the API and returns back the information found.
        """
        latitude = self.latitude_value.get()
        longitude = self.longitude_value.get()

        try:
            latitude = int(latitude)
            longitude = int(longitude)
            if -90 <= latitude <= 90 and -180 <= longitude <= 180:
                pass
            else:
                raise ValueError
            
        except ValueError:
            self.error.place(x = 500, y = 180)

        except TypeError:
            self.error.place(x = 500, y = 180)

        else:
            self.error.place_forget()