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

## Failed Attempt trying to import PIL
# bg = ImageTk.PhotoImage(Image.open("space.png"))
# root.create_image(0, 0, anchor=NW, image=bg)

# Button Hovering Time!
style = ttk.Style()
style.configure("Greet.TButton", background="white", foreground="black", font=("Arial", 10))
style.map("Greet.TButton", background=[("active", "#E066FF")])

## Failed Attempt using functions bc Mac doesnt like tkinter
# def onHover(e):
#     submit["background"] = "#E066FF"
#     print("onHover!!")
# def offHover(e):
#     submit["background"] = "white"
#     print("Off Hover!")

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
userLanguage['values'] = ["Galactic Basic Standard", "Greek", "Huttese", "Mando'a", "Shyriiwook", "Spanish"]
userLanguage.current(0) 
userLanguage.pack()

# ----- Submit
submit = ttk.Button(root, text="Greet Me", command=submitForm, style="Greet.TButton")
submit.pack(pady=(50, 30))
# submit.bind("<Enter>", onHover)
# submit.bind("<Leave>", offHover)

# ----- Output Section
output = tk.Label(  root, 
                    text = "",
                    bg = "black",
                    fg = "white",
                    font = ("Arial", 16)
                  )
output.pack()

root.mainloop()