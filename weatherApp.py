import tkinter as tk
from tkinter import ttk

# Main App Information
root = tk.Tk() 
root.title("PCC Weather App")
root.geometry("650x250")

# First Row: label, entry box and button

locationLabel = tk.Label(root, text="Location: ", padx=10, pady=5)
locationLabel.grid(row=0, column=0)

locationEntry = tk.Entry(root)
locationEntry.grid(row=0, column=1, padx=10)

updateButton = tk.Button(root, text="Find Weather")
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

root.mainloop()