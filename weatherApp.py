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

root.mainloop()