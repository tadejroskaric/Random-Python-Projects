import tkinter as tk
import tkinter.font as font


def convert():
    celsius = float(temp_ent.get())*(9/5) + 32
    lbl_result["text"] = float(celsius)


window = tk.Tk()
window.geometry("500x30")
window.title("Temperature converter")

window.columnconfigure([0, 1], minsize=10)
window.rowconfigure(0, minsize=10)

myfont = font.Font(size=20)
temp_ent = tk.Entry(font=myfont)
temp_ent.grid(row=0, column=0, sticky="n", )


label_celsius = tk.Label(text="°C", font=myfont)
label_celsius.grid(row=0, column=1, sticky="n")

convert_btn = tk.Button(text="\N{RIGHTWARDS BLACK ARROW}", width=5, pady=7, padx=10, command=convert)
convert_btn.grid(row=0, column=3, sticky="n")

lbl_result = tk.Label(font=myfont)
lbl_result.grid(row=0, column=4, sticky="n")

lbl_fahrenheit = tk.Label(text="°F", font=myfont)
lbl_fahrenheit.grid(row=0, column=5, sticky="n")


window.mainloop()
