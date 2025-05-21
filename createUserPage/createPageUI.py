import tkinter as tk
from tkinter import ttk

class createPageUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Your Own HTML!")
        self.root.geometry("700x700")

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