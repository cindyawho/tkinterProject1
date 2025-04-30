import tkinter as tk
from ttkthemes import ThemedTk # type: ignore
from tkinter import ttk
import time # for fun :)

# Main App Information
root = ThemedTk(theme="radiance")
root.title("Ordering Kiosk")

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

        # Error Handling
        self.nameResultLabel = ttk.Label(self.root, text="")
        self.nameResultLabel.grid(row=6, column=0, columnspan=5, padx=10, pady=10)

        self.foodResultLabel = ttk.Label(self.root, text="")
        self.foodResultLabel.grid(row=7, column=0, columnspan=5, padx=10, pady=10)
    
    def checkName(self):
        customerName = self.nameEntry.get()
        if customerName == "":
            self.nameResultLabel.config(text="Error: Please Enter a Name.", foreground="red")
            return False
        else:
            return customerName
    
    def checkEntree(self):
        entreeName = self.foodOption.get()
        if entreeName == "":
            self.foodResultLabel.config(text="Error: Please Select an Entree.", foreground="red")
            return False
        else:
            return entreeName
    
    def order(self):
        # reset text to erase weird overlapping label texts
        self.nameResultLabel.config(text="                                                     ")
        self.foodResultLabel.config(text="                                                     ")
        self.nameResultLabel.update_idletasks()

        print("Customer ordered")
        self.nameResultLabel.config(text="Order Processing...", foreground="blue")
        self.nameResultLabel.update_idletasks()  # force update, otherwise mainloop keeps going and won't show order processing bit
        time.sleep(2)
        name = self.checkName()
        entree = self.checkEntree()
        if name and entree:
            self.nameResultLabel.config(text=f"Thank you {name}. Your order is coming up shortly!", foreground="green")
            self.nameResultLabel.update_idletasks()
            time.sleep(2)
            self.foodResultLabel.config(text=f"Here's your {entree}!", foreground="green")
            self.foodResultLabel.update_idletasks()

app = OrderingKiosk(root)
root.mainloop()