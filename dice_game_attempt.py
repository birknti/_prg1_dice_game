import random
import time
import tkinter as tk
from tkinter import font


def Spin(spinner=0):

    global x
    bounce = random.choice([1, 2])
    if spinner < 10:
        x = random.randint(1, 6)
        print(f" tärning1\r{x}", end="", flush=True)
        spinning.config(text=f"{x}")
        window.after(150, Spin, spinner + bounce)
        return

    print(f"Första tärningen blev {x}")
    result.config(text=f"Din första tärning blev {x}") 

def Quit():

    result.config(text=f"Du fick totalt{x}")

    
    

window = tk.Tk()
window.title("Gamble")
window.geometry("550x300")

result = tk.Label(window, text="")
result.pack()


spinning = tk.Label(window, text="This is the dice")
spinning.pack()

result.config(text="")

button = tk.Button(window, text="Spin", command=Spin)
button.pack()

button = tk.Button(window, text="Give up", command=Quit)
button.pack()

 
window.mainloop()