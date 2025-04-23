import tkinter as tk

def buttonClick():
    label.config(text = "WRONG LEVEERRRR")

def changeName():
    inputName = name.get()
    label.config(text = f'Pull the lever, {inputName}!')

root = tk.Tk() # creating Tk object which will be our root

name = tk.Entry(root)
name.pack()
nameButton = tk.Button(root, text="Change Name", command = changeName)
nameButton.pack()

root.title("Pull the Lever!")

label = tk.Label(root, text = "Pull the lever, Kronk!")
label.pack()

button = tk.Button(root, text="The Lever", command = buttonClick)
button.pack()

root.mainloop()

# to run, in terminal write
# python leverapp.py