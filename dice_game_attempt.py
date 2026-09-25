import random
import time
import tkinter as tk
from tkinter import font

global x
global prize
global cost


money = 100


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
    result.config(text=f"Din tärning blev {x}") 

def Quit():

    result.config(text=f"Du fick totalt{prize} mynt")

def first():
    global money, cost, prize

    try:
        cost = int(cost_entry.get())
    except ValueError:
        result.config(text="Type a whole number for the cost")
        return

    if cost <= 0 or cost > money:
        result.config(text=f"Choose a cost between 1 and {money}")
        return

    money -= cost
    prize = cost * 10
    result.config(text=f"You paid {cost}. You have {money} coins left.")
    Spin()

    




window = tk.Tk()
window.title("Gamble")
window.geometry("550x300")

result = tk.Label(window, text="")
result.pack()

cost_entry = tk.Entry(window)
cost_entry.pack()

spinning = tk.Label(window, text="This is the dice")
spinning.pack()

button = tk.Button(window, text="Spin", command=first)
button.pack()

button = tk.Button(window, text="Give up", command=Quit)
button.pack()

 
window.mainloop()