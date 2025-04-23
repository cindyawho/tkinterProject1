import tkinter as tk

def buttonClick():
    label.config(text = "WRONG LEVEERRRR")

root = tk.Tk() # creating Tk object which will be our root

root.title("Pull the Lever!")

label = tk.Label(root, text = "Pull the lever, Kronk!")
label.pack()

button = tk.Button(root, text="The Lever", command = buttonClick)
button.pack()

root.mainloop()

# to run, in terminal write
# python leverapp.py