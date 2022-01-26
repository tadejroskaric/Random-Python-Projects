import random
import tkinter as tk
import tkinter.font as font


def roll():
    roll_value = random.randint(1, 6)
    lbl_value["text"] = roll_value


window = tk.Tk()
window.title("Dice roller")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

myfont = font.Font(size=20)
btn = tk.Button(text="Roll", width=10, height=2, font=myfont, command=roll)
btn.pack()

lbl_value = tk.Label(text="", font=myfont)
lbl_value.pack()

window.mainloop()
