import tkinter as tk
from tkinter import ttk
import weatherAPI as wapi

class WeatherForecast:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecaster")
        self.root.geometry("700x300")
        # first row elements
        self.locations = ["Pasadena", "New York", "Chicago", "San Francisco"]
        self.location_combobox = ttk.Combobox(root, values=self.locations,
        font=("Helvetica", 12))
        self.location_label = ttk.Label(self.root, text="Select Location:",
        font=("Helvetica", 12))
        self.location_label.grid(row=0, column=0, padx=10, pady = 10)
        self.location_combobox.grid(row=0, column=1, padx=10, pady = 10)
        self.location_button = ttk.Button(self.root, text="Get Forecast",
        command=self.get_weather)
        self.location_button.grid(row=0, column=2, padx=10, pady = 10)
        #second row elements
        self.weather_label = ttk.Label(self.root, text="Current Temperature: N/A",
        font=("Helvetica", 20))
        self.weather_label.grid(row=1, column=0, columnspan=2, padx=10, pady = 10)
        self.weather_image = tk.Label(root, image='')
        self.weather_image.grid(row=1, column=3, padx=10, pady = 10)
        #third row elements
        self.high_temp_label = tk.Label(self.root, text="Detailed Forecast: N/A",
        font=("Helvetica", 12), wraplength=300, justify='left')
        self.high_temp_label.grid(row=2, column=0, columnspan=2, padx=10, pady =
        10)
        self.low_temp_label = ttk.Label(self.root, text="Chance of Rain: N/A",
        font=("Helvetica", 12))
        self.low_temp_label.grid(row=2, column=3, padx=10, pady = 10)
        self.sun_image = tk.PhotoImage(file='../sun.png')
        self.sun_image = self.sun_image.subsample(5)
        self.rain_image = tk.PhotoImage(file='../rain.png')
        self.rain_image = self.rain_image.subsample(10)
    def get_weather(self):
        location = self.location_combobox.get()
        # determine location and api call
        if location == "Pasadena":
            temp, detail, precipitation = wapi.get_weather(160, 49, 'LOX')
        elif location == "New York":
            temp, detail, precipitation = wapi.get_weather(36, 36, 'OKX')
        elif location == "Chicago":
            temp, detail, precipitation = wapi.get_weather(67, 93, 'LOT')
        elif location == "San Francisco":
            temp, detail, precipitation = wapi.get_weather(83, 104, 'MTR')
        # update the labels based on API response
        self.weather_label.config(text=f"Current temperature: {temp}F")
        if precipitation:
            self.low_temp_label.config(text=f"Chance of Precipitation:{precipitation}%")
            if precipitation> 50:
                self.weather_image.config(image=self.rain_image)
            else:
                self.weather_image.config(image=self.sun_image)
        else:
            self.weather_image.config(image=self.sun_image)
            self.low_temp_label.config(text=f"Chance of Precipitation: 0%")
        self.high_temp_label.config(text=f"Detailed Forecast: {detail}")