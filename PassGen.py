
from lib2to3.pygram import Symbols
from tkinter import *
import random, string


window = Tk()
window.geometry("250x250+700+100")
window.title("assword Generator")

title = StringVar()
label = Label(window, textvariable = title)
label.pack()
title.set("The strength of our password")

choice = IntVar()

def selection():
    pass

R1 = Radiobutton(window, text="POOR", variable=choice, value=1, command=selection)
R1.pack(anchor=CENTER)

R2 = Radiobutton(window, text="AVERAGE", variable=choice, value=2, command=selection)
R2.pack(anchor=CENTER)

R3 = Radiobutton(window, text="ADVANCED", variable=choice, value=3, command=selection)
R3.pack(anchor=CENTER)

lenlabel = StringVar()
lenlabel.set("Password Length")
lentitle = Label(window, textvariable=lenlabel)
lentitle.pack()

val = IntVar()
spinlength = Spinbox(window, from_=8, to_=24, textvariable=val, width=13)
spinlength.pack()

def callback():
    lsum.config(text=passgen())
    
passgenButton = Button(window, text="Generate Password", bd=5, height=2, command=callback, pady=3)
passgenButton.pack()

lsum = Label(window, text="")
lsum.pack()

poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+=[]{}\\:;"'<>,.?/"""
advance = poor + average + symbols

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))


window.mainloop()