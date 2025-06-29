import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~ STYLING ~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
root.geometry("500x500")
root.config(background = "Black") 

# Successful attempt on online compiler
bg = tk.PhotoImage(file="space.png")
background_label = tk.Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Button Hovering Time!
style = ttk.Style()
style.configure("Greet.TButton", background="white", foreground="black", font=("Arial", 10))
style.map("Greet.TButton", background=[("active", "#E066FF")])

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~ FUNCTIONS ~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

languageDict = {
                "Huttese": "H'chu apenkee", 
                "Mando'a" : "Su'cuy'gar",
                "Galactic Basic Standard": "Hello",
                "Shyriiwook" : "Wyaaaaaa",
                "Greek" : "Γειά σου",
                "Spanish" : "Hola"
                }

resistanceDict = {
                "Huttese": "Chuba kava doth wa Resistance",
                "Mando'a": "Olarom at te Werda",
                "Galactic Basic Standard": "Welcome to the Resistance",
                "Shyriiwook": "Wyaaaaaa raaaaaahhgh raaaaaawwwr",
                "Greek": "Καλώς ήρθες στην Αντίσταση",
                "Spanish": "Bienvenido a la Resistencia"
                }

def submitForm():
    userName = name.get()
    if userName == "":
        output.config(text=f'Please input a name.')
    else:
        userLang = userLanguage.get()
        greeting = languageDict[userLang]
        output.config(text=f'{greeting}, {userName}\n {resistanceDict[userLang]}')

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~ Start of UI ~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ----- Name Section
nameText = tk.Label(root, 
                    text = "What should we call you rebel?",
                    bg = "black",
                    fg = "white",
                    font = ("Courier New", 16)
                    )
nameText.pack(pady=(50, 20))

name = tk.Entry(root)
name.pack()

# ----- Language Section
languageText = tk.Label(root, 
                        text = "Which language do you prefer?", 
                        bg = "black",
                        fg = "white",
                        font = ("Courier New", 16)
                        )
languageText.pack(pady=20)

userLanguage = ttk.Combobox(root)
userLanguage['values'] = ["Galactic Basic Standard", "Greek", "Huttese", "Mando'a", "Shyriiwook", "Spanish"]
userLanguage.current(0) 
userLanguage.pack()

# ----- Submit
submit = ttk.Button(root, text="Greet Me", command=submitForm, style="Greet.TButton")
submit.pack(pady=(50, 30))

# ----- Output Section
output = tk.Label(  root, 
                    text = "",
                    bg = "black",
                    fg = "white",
                    font = ("Courier New", 16)
                  )
output.pack()

root.mainloop()