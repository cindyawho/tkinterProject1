import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~ FUNCTIONS ~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def submitForm():
    userName = name.get()

    output.config(text=f'Hello, {userName}')

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~ Start of UI ~~~~~~~~~~~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ----- Name Section
nameText = tk.Label(root, text = "Welcome to the resistance. What should we call you rebel?")
nameText.pack()

name = tk.Entry(root)
name.pack()

# ----- Language Section
languageText = tk.Label(root, text = "Which language do you prefer?")
languageText.pack()

userLanguage = ttk.Combobox(root)
userLanguage['values'] = ["Galactic Basic Standard", "Greek", "Huttese", "Mando’a", "Shyriiwook", "Spanish"]
userLanguage.current(0) 
userLanguage.pack()

# Huttese: "H'chu apenkee"
# Mando'a: "Su'cuy'gar" 
# Galactic Basic Standard: Hello
# Shyriiwook is "Wyaaaaaa

# ----- Submit
submit = tk.Button(root, text = "Submit", command = submitForm)
submit.pack()

# ----- Output Section
output = tk.Label(root, text = "")
output.pack()

root.mainloop()

#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  ~~~~ Greeting Application Guidelines ~~~~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# The objective of this assignment is to create a 
# simple greeting application using Python's Tkinter library. 
# The application should allow users to input their name, 
# select their preferred language for the greeting, 
# and display a personalized greeting message.

# Requirements:

# 1. Create a GUI application using Tkinter that includes the following components:
#    - Label prompting the user to enter their name.
#    - Entry widget for users to input their name.
#    - Label prompting the user to select their preferred language.
#    - Combobox (dropdown menu) for users to select their preferred language from a list of options (e.g., English, French, Spanish).
#    - Button labeled "Greet Me" that, when clicked, generates a personalized greeting message based on the user's input.

# 2. Implement functionality to display a greeting message based on the user's input:
#    - When the "Greet Me" button is clicked, the application should generate a greeting message that includes the user's name and is displayed in the selected language.

# 3. Apply styling and formatting to the GUI components to enhance the visual appeal of the application:
#    - Use appropriate font styles, sizes, and colors for labels, entry widgets, combobox, button, and greeting message.

# Scoring Rubric:

# 1. GUI Components (3 points):
#    - Label prompting the user to enter their name.
#    - Entry widget for name input.
#    - Label prompting the user to select their preferred language.
#    - Combobox for language selection.
#    - "Greet Me" button.

# 2. Functionality (4 points):
#    - Application generates a personalized greeting message.
#    - Greeting message includes the user's name.
#    - Greeting message is displayed in the selected language.
#    - Proper handling of edge cases (e.g., empty name input).

# 3. Styling and Formatting (3 points):
#    - Use of appropriate font styles, sizes, and colors for GUI components.
#    - Consistent alignment and spacing of components.
#    - Overall visual appeal and user-friendliness of the application.


# *Note: Bonus points may be awarded for implementing additional features or enhancements beyond the basic requirements.*
