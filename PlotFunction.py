from turtle import fillcolor
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

window = Tk()
WIDTH = 1000
HEIGHT = 700
window.title("Function Plotter")
window.geometry(f"{WIDTH}x{HEIGHT}")
def hSeparator(rowNum):
    ttk.Separator(window, orient='horizontal').pack(fill='x',padx=5)

# Main title
lMain = Label(window,text="Function Plotter",bg="#00FFFF")
lMain.config(font=('Arial',40))
lMain.pack(fill=X,ipady=20)

# Horizontal separator
hSeparator(1)

# Labels
l1 = Label(window,text="Enter the function:")
l1.pack(side=TOP,anchor=NW,padx=5,pady=10)
l2 = Label(window,text="minimum value of x")
l2.pack(padx=5,pady=10)
l3 = Label(window,text="maximum value of x")
l3.pack(side='left',padx=5,pady=10)

# Text
func = Entry(window, width= 30, borderwidth=0)
func.pack(side='right',padx=10,pady=10)
minX = Entry(window, width= 20)
minX.pack(padx=10,pady=10)
maxX = Entry(window, width= 20)
maxX.pack(side='left', padx=10,pady=10)

window.mainloop()

