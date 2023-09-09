#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from appeal_calculator import AppealCalculator


def write_date():
    mydate = entry.get()
    hatarozat1 = AppealCalculator(mydate)
    hatarozat1.Holidays()
    mytext = hatarozat1.endday
    label_2.config(text=f"A határidő {mytext} napján végződik")


root = tk.Tk()
root.title("Határidő számító")

label_1 = tk.Label(
    root, text="Írja be a határozat időpontját kötőjelekkel elválasztva!", padx=10, pady=10,
    font=("Times", 11))
label_1.pack()

entry = tk.Entry(root, font=("Times", 11))
entry.pack()

button = tk.Button(root, text="OK", command=write_date, font=("Times", 10))
button.pack(pady=5)

label_2 = tk.Label(root, text="", font=("Times", 11))
label_2.pack()

root.mainloop()
