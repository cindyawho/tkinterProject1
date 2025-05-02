import tkinter as tk
from ttkthemes import ThemedTk # type: ignore
from tkinter import ttk
import time # for fun :)
from PIL import Image, ImageTk # type: ignore 
# pip install pillow

# Main App Information
root = ThemedTk(theme="radiance")
root.title("Cindy's Ordering Kiosk")

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

        # ~~~~~~~~Ordering Details~~~~~~~~~
        self.foodLabel = ttk.Label(self.root, text="Entree: ")
        self.foodLabel.grid(row=2, column=0, padx=10, pady=20)

        self.foodOption = ttk.Combobox(self.root)
        self.foodOption['values'] = ["", "Albondigas", "Burger", "Lasagna", "Pad See Ew", "Pizza", "Pupusa", "Quesadilla"]
        self.foodOption.current(0)
        self.foodOption.grid(row=2, column=1, padx=10)

        self.wantsDrink = tk.BooleanVar()
        self.checkbox = ttk.Checkbutton(
            root,
            text='Add Drink',
            variable=self.wantsDrink
        )
        self.checkbox.grid(row = 2, column=2, padx=10)

        self.button = ttk.Button(self.root, text="Order", command=self.order)
        self.button.grid(row=5, column=0, columnspan=3, padx=10)

        # Error Handling and Results
        self.nameResultLabel = ttk.Label(self.root, text="")
        self.nameResultLabel.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

        self.foodResultLabel = ttk.Label(self.root, text="")
        self.foodResultLabel.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

        # Images
        pil_Kiosk = Image.open("OrderingKiosk/images/kiosk.jpg").resize((400, 250), Image.LANCZOS)
        self.kiosk_image = ImageTk.PhotoImage(pil_Kiosk)
        self.kioskImage = ttk.Label(root, image=self.kiosk_image)
        self.kioskImage.grid(row=0, column=3, rowspan=5, columnspan=2)

        pil_image = Image.open("OrderingKiosk/images/plate.webp").resize((200, 150), Image.LANCZOS)
        self.food_image = ImageTk.PhotoImage(pil_image)
        self.foodImage = ttk.Label(root, image=self.food_image)
        self.foodImage.grid(row=6, column=3, rowspan=2)

        self.pil_drink = Image.open("OrderingKiosk/images/square.jpg").resize((150, 150), Image.LANCZOS)
        self.drink_image = ImageTk.PhotoImage(self.pil_drink)
        self.drinkImage = ttk.Label(root, image=self.drink_image)
        self.drinkImage.grid(row=6, column=4, rowspan=2)

    # ~~~~~~~~~ Functions ~~~~~~~~~~~
    # Error Handling for name and entree
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
    
    # Create Image depending on entree
    def createImage(self, entree):
        if entree == "Pad See Ew": entree = "padSeeEw"
        pil_image = Image.open(f"OrderingKiosk/images/{entree}.webp").resize((200, 150), Image.LANCZOS)
        self.food_image = ImageTk.PhotoImage(pil_image)
        return self.food_image
    
    # Create image if user wants drink
    def createDrinkImage(self):
        if self.wantsDrink.get():
            pil_image = Image.open(f"OrderingKiosk/images/drink.png").resize((200, 150), Image.LANCZOS)
            self.drink_image = ImageTk.PhotoImage(pil_image)
            return self.drink_image
        else: 
            pil_image = Image.open("OrderingKiosk/images/square.jpg").resize((150, 150), Image.LANCZOS)
            self.drink_image = ImageTk.PhotoImage(pil_image)
            return self.drink_image

    # Main Ordering Function
    def order(self):
        # reset text and image to erase weird overlapping label texts
        # self.nameResultLabel.config(text="                                                     ")
        # self.foodResultLabel.config(text="                                                     ")
        foodImg = self.createImage("plate")
        self.foodImage.config(image=foodImg)
        self.foodImage.image = foodImg # Something about Garbage Collection - to read later!
        self.drinkImage.config(image=self.drink_image)
        self.drinkImage.image = self.drink_image # Something about Garbage Collection - to read later!
        self.nameResultLabel.update_idletasks()

        print("Customer ordered")
        self.nameResultLabel.config(text="Order Processing...", foreground="blue")
        self.nameResultLabel.update_idletasks()  # force update, otherwise mainloop keeps going and won't show order processing bit
        time.sleep(2)
        name = self.checkName()
        entree = self.checkEntree()
        if name and entree:
            self.nameResultLabel.config(text=f"Your order is coming up shortly!", foreground="green")
            self.nameResultLabel.update_idletasks()
            time.sleep(2)
            drinkImg = self.createDrinkImage()
            self.drinkImage.config(image=drinkImg)
            self.foodResultLabel.config(text=f"Here's your {entree} meal, {name}!", foreground="green")
            foodImg = self.createImage(entree)
            self.foodImage.config(image=foodImg)

app = OrderingKiosk(root)
root.mainloop()