import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from math import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# creating a window
window = Tk()
WIDTH = 1000
HEIGHT = 500
window.title("Function Plotter")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(False, False)

# placeholder for text boxes
# def place_holder(textBoxObj,ph):
#     textBoxObj.insert(0,ph)
#     textBoxObj.configure(state=DISABLED)
#     textBoxObj.bind('<Button-1>', lambda event: on_click(event,textBoxObj))
# def on_click(event,textBoxObj):
#     textBoxObj.configure(state=NORMAL)
#     textBoxObj.delete(0, END)
#     textBoxObj.unbind('<Button-1>', on_click)

# Assertions
# validate the function
def validateFunction(f_of_x,minValue,maxValue):
    f_of_x = f_of_x.replace("^","**")
    f_of_x = f_of_x.replace("X","x")
    f_of_x = f_of_x.replace("sin","np.sin")
    f_of_x = f_of_x.replace("cos","np.cos")
    try:
        x = np.linspace(minValue,maxValue)
        return eval(f_of_x),True
    except:
        popup("Please, Enter a valid function")
        return 

# validate min and max values and return them as floats
isValid2 = False
def validateX(a,b):
    try:
        a = float(a)
        b = float(b)
    except:
        popup('Please, Enter a number in both fields')
        return
    if(a>b):
        popup('Please, make sure that \nminimum x smaller than maximum x')
        return
    else:
        return a,b

# Plotting 
def plotting():
    f_of_x = func.get()
    minValue = minX.get()
    maxValue = maxX.get()
    minmax = validateX(minValue,maxValue)
    equ,plot = validateFunction(f_of_x,minmax[0],minmax[1])
    if(type(minmax[0])==float and type(minmax[1])==float and plot):
        x = np.linspace(minmax[0],minmax[1])
        y = equ
        fig = plt.Figure(figsize=(6,4), dpi=100)
        ax = fig.add_subplot()
        ax.plot(x,y, color = 'g')
        canvas = FigureCanvasTkAgg(fig, window) 
        can1 = canvas.get_tk_widget()
        can1.place(height=380,x=375,y=112) 
        ax.axhline(y=0, color='black')
        ax.axvline(x=0, color='black')
        ax.grid(color='black',linewidth=0.1)

# clear the plot 
def clearfunc():
    list = window.place_slaves()
    for i in list:
        if(str(type(i))=="<class 'tkinter.Canvas'>"):
            i.destroy()

# Error pop-up window
def popup(errorTxt):
   smallWin= Toplevel(window)
   smallWin.geometry("200x100")
   smallWin.title("Error!")
   Label(smallWin, text= errorTxt).pack(ipady=45)

# Main title
lMain = Label(window,text="Function Plotter",bg="#00FFFF")
lMain.config(font=('Arial',40))
lMain.pack(fill=X,ipady=20)

# Horizontal separator
ttk.Separator(window, orient='horizontal').pack(fill=X,padx=5)

# Label for f(x) & its textbox
l1 = Label(window,text="Enter the function:")
l1.pack(anchor=NW,padx=5,pady=5)
func = Entry(window, width= 30, borderwidth=1)
# place_holder(func,"Enter a function eg: x^2")
func.pack(anchor=NW,padx=10,pady=5)

# Label for minimum value of x & its textbox
l2 = Label(window,text="minimum value of x") 
l2.pack(anchor=NW,padx=5,pady=5)
minX = Entry(window, width= 30, borderwidth=1)
# place_holder(minX,"Enter a number eg: -10")
minX.pack(anchor=NW,padx=10,pady=5)

# Label for maximum value of x & its textbox
l3 = Label(window,text="maximum value of x")
l3.pack(anchor=NW,padx=5,pady=5)
maxX = Entry(window, width= 30, borderwidth=1)
# place_holder(maxX,"Enter a number eg: 10")
maxX.pack(anchor=NW,padx=10,pady=5)

# Clear Button
clBtn = Button(window, text="Clear",command = clearfunc,bg="#DB524B",width=8)
clBtn.pack(side=LEFT,padx=50)

# Plot Button
plBtn = Button(window, text="Plot",command = plotting,bg="#7bd500",width=15)
plBtn.pack(side=LEFT,padx=15)

# vertical separator
ttk.Separator(window, orient='vertical').place(x=350,y=305,anchor = CENTER,height=380)

window.mainloop()

