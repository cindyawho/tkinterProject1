import tkinter as tk
from tkinter import ttk

# Utility Functions
def updateWeather():
    location = locationEntry.get()
    if location.lower() == "pasadena":
        weatherLabel.config(text=f"Current Weather in {location}: Sunny") 
        weatherImage.config(image=sunImage)
        highTempLabel.config(text=f"High: 82")
        lowTempLabel.config(text=f"Low: 65")
    elif location.lower() == "seattle":
        weatherLabel.config(text=f"Current Weather in {location}: Rainy") 
        weatherImage.config(image=rainImage)
        highTempLabel.config(text=f"High: 65")
        lowTempLabel.config(text=f"Low: 45")
    else:
        weatherLabel.config(text=f"Error: {location} not found. Please enter a Valid Location.")

# Main App Information
root = tk.Tk() 
root.title("PCC Weather App")
root.geometry("650x250")

# First Row: label, entry box and button

locationLabel = tk.Label(root, text="Location: ", padx=10, pady=5)
locationLabel.grid(row=0, column=0)

locationEntry = tk.Entry(root)
locationEntry.grid(row=0, column=1, padx=10)

updateButton = tk.Button(root, text="Find Weather", command=updateWeather)
updateButton.grid(row=0, column=2)

# Second Row: text and image

weatherLabel = tk.Label(root, text="Current Weather: N/A")
weatherLabel.grid(row=1, column=0, columnspan=3)

weatherImage = tk.Label(root, image="")
weatherImage.grid(row=1, column=3)

# Third Row: high temp and low temp
highTempLabel = tk.Label(root, text="High: N/A")
highTempLabel.grid(row=2, column=0, columnspan=2)

lowTempLabel = tk.Label(root, text="Low: N/A")
lowTempLabel.grid(row=2, column=2, columnspan=2)

#Images:
sunImage = tk.PhotoImage(file="sun.png")
sunImage = sunImage.subsample(16)

rainImage = tk.PhotoImage(file="rain.png")
rainImage = rainImage.subsample(16)

root.mainloop()