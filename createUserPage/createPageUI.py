import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

# Used https://customtkbuilder.com/

class CreatePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Your Own HTML Site!")
        self.root.geometry("700x700")
        self.root.configure(bg="#B8FFFA")
        # Styling
        style = ttk.Style()
        style.configure("title.TLabel", foreground="black", background="#B8FFFA", font=('Courier New', 18))
        style.configure("text.TLabel", foreground="black", background="#B8FFFA", font=('Arial', 14))
        style.configure("note.TLabel", foreground="#FF4255", background="#B8FFFA", font=('Arial', 12))
        style.configure("TEntry", foreground = "blue")

        # HTML Title
        self.greetLabel = ttk.Label(self.root, text="Hello! Let's create your very own HTML page!", style="title.TLabel")
        self.greetLabel.grid(row=0, column=0, columnspan=5, pady=20, padx=20)

        # User Inputs for HTML Page
        self.nameLabel = ttk.Label(self.root, text="Name: ", style="text.TLabel")
        self.nameLabel.grid(row=1, column=0, columnspan=2, pady=20, padx=20)
        self.nameEntry = ttk.Entry(self.root, style="TEntry", width=50)
        self.nameEntry.grid(row=1, column=1, columnspan=3, pady=20, padx=20)

        self.hobbiesLabel = ttk.Label(self.root, text="Hobbies: ", style="text.TLabel")
        self.hobbiesLabel.grid(row=2, column=0, columnspan=2, pady=20, padx=20)
        self.hobbiesEntry = ttk.Entry(self.root, style="TEntry", width=50)
        self.hobbiesEntry.grid(row=2, column=1, columnspan=3, pady=20, padx=20)

        self.hobbyNoteLabel = ttk.Label(self.root, text="*Note: Please separate each hobby with a comma. ", style="note.TLabel")
        self.hobbyNoteLabel.grid(row=3, column=0, columnspan=4, padx=20)

         # CSS Title
        self.greetLabel = ttk.Label(self.root, text="Time to Style Your Site! If you prefer, \nyou can use our default styling.", style="title.TLabel")
        self.greetLabel.grid(row=4, column=0, columnspan=5, pady=(75, 20), padx=20)
        # CSS Use Default
        self.agree = tk.BooleanVar(self.root, True)
        self.checkbox = ttk.Checkbutton(
            self.root,
            text='Use Default Styling - If checked, you can skip the next CSS inputs and default styling will be used.',
            command=self.checkCSSChoice,
            variable=self.agree
        )
        self.checkbox.grid(row=5, column=0, columnspan=5, pady=20, padx=20)

        # User Inputs for CSS
        self.bgColorLabel = ttk.Label(self.root, text="Background Label: ", style="text.TLabel")
        self.bgColorLabel.grid(row=6, column=0, columnspan=2, pady=20, padx=20)
        self.bgColorButton = ttk.Button(self.root, text='Select a BackgroundColor', command=self.changeColor)
        self.bgColorButton.grid(row=6, column=1, columnspan=3, pady=20, padx=20)
        self.colorLabel = ttk.Label(self.root, text=".   color   .", style="text.TLabel")
        self.colorLabel.grid(row=6, column=3, columnspan=2, pady=20, padx=20)

    # ~~~~~~~~~~~~ Form Functions ~~~~~~~~~~~~~~~
    # color picker
    def changeColor(self):
        colors = askcolor(title="Tkinter Color Chooser")
        # print(colors)
        self.colorLabel.configure(background=colors[1])

    # default or user Styling
    def checkCSSChoice(self):
        # print(self.agree.get())
        if self.agree.get():
            print("Use Default Styling")
        else:
            print("User will input their CSS Choices")

    def writeFile():
        with open('index.html', 'r+') as f:
            sent1 = f.readline()
            sent2 = f.readline()
            f.write('\n')
            f.write('<html></html>')
        # OR ...
        # f = open('index.html') # open html file
        # f.close()

    def readFile():
        f = open('index.html')
        contents = f.read() # reads file text into string
        print(contents)
        f.close()