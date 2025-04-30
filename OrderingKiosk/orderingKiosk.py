import tkinter as tk
from ttkthemes import ThemedTk # type: ignore
from tkinter import ttk

# Main App Information
root = ThemedTk(theme="radiance")

class OrderingKiosk():
    def __init__(self, root):
        self.root = root
        self.greetLabel = ttk.Label(self.root, text="Hello, Customer!", justify="center")
        self.greetLabel.grid(row=0, column=0, columnspan=3, pady=20)

        # Customer Info
        self.nameLabel = ttk.Label(self.root, text="Name: ")
        self.nameLabel.grid(row=1, column=0, padx=10, pady=20)

        self.nameEntry = ttk.Entry(self.root)
        self.nameEntry.grid(row=1, column=1, padx=10)

        # Ordering Details
        self.foodLabel = ttk.Label(self.root, text="Entree: ")
        self.foodLabel.grid(row=2, column=0, padx=10, pady=20)

        self.foodOption = ttk.Combobox(self.root)
        self.foodOption['values'] = ["", "Albondigas", "Burger", "Lasagna", "Pad See Ew", "Pizza", "Pupusa", "Quesadilla"]
        self.foodOption.current(0)
        self.foodOption.grid(row=2, column=1, padx=10)

        self.button = ttk.Button(self.root, text="Order", command=self.order)
        self.button.grid(row=5, column=0, columnspan=3, padx=10)
    
    def checkName(self):
        customerName = OrderingKiosk.nameEntry.get()
    def order(self):
        print("Customer ordered")

app = OrderingKiosk(root)
root.mainloop()