import weatherUI as wui
import tkinter as tk
if __name__ == "__main__":
    root = tk.Tk()
    app = wui.WeatherForecast(root)
    root.mainloop()