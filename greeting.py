import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~ STYLING ~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
root.geometry("500x500")
root.config(background = "Black") 

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~ FUNCTIONS ~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

languageDict = {
                "Huttese": "H'chu apenkee", 
                "Mando'a" : "Su'cuy'gar",
                "Galactic Basic Standard": "Hello",
                "Shyriiwook" : "Wyaaaaaa",
                "Greek" : "Yassou",
                "Spanish" : "Hola"
                }

def submitForm():
    userName = name.get()
    if userName == "":
        output.config(text=f'Please input a name.')
    else:
        userLang = userLanguage.get()
        greeting = languageDict[userLang]
        output.config(text=f'{greeting}, {userName}\n Welcome to the resistance.')

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~ Start of UI ~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ----- Name Section
nameText = tk.Label(root, 
                    text = "What should we call you rebel?",
                    bg = "black",
                    fg = "white",
                    font = ("Arial", 16)
                    )
nameText.pack(pady=(50, 20))

name = tk.Entry(root)
name.pack()

# ----- Language Section
languageText = tk.Label(root, 
                        text = "Which language do you prefer?", 
                        bg = "black",
                        fg = "white",
                        font = ("Arial", 16)
                        )
languageText.pack(pady=20)

userLanguage = ttk.Combobox(root)
userLanguage['values'] = ["Galactic Basic Standard", "Greek", "Huttese", "Mando’a", "Shyriiwook", "Spanish"]
userLanguage.current(0) 
userLanguage.pack()

# ----- Submit
submit = tk.Button(root, text = "Greet Me", command = submitForm)
submit.pack(pady=(50, 30))

# ----- Output Section
output = tk.Label(root, text = "")
output.pack()

root.mainloop()
