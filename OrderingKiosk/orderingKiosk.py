import tkinter as tk
from ttkthemes import ThemedTk # type: ignore
from tkinter import ttk

# Main App Information
root = ThemedTk(theme="radiance")

class OrderingKiosk():
    def order():
        print("Customer ordered")

    greetLabel = ttk.Label(root, text="Hello, Customer!", justify="center")
    greetLabel.grid(row=0, column=0, columnspan=3, pady=20)

    # Customer Info
    nameLabel = ttk.Label(root, text="Name: ")
    nameLabel.grid(row=1, column=0, padx=10, pady=20)

    button = ttk.Button(root, text="Order", command=order)
    button.grid(row=2, column=0, columnspan=3, padx=10)

root.mainloop()