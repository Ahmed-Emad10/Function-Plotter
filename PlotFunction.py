import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from math import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


window = Tk()
WIDTH = 1000
HEIGHT = 500
window.title("Function Plotter")
window.geometry(f"{WIDTH}x{HEIGHT}")


def place_holder(textBoxObj,ph):
    textBoxObj.insert(0,ph)
    textBoxObj.configure(state=DISABLED)
    textBoxObj.bind('<Button-1>', lambda event: on_click(event,textBoxObj))
def on_click(event,textBoxObj):
    textBoxObj.configure(state=NORMAL)
    textBoxObj.delete(0, END)
    textBoxObj.unbind('<Button-1>', on_click)

# clear the plot 
x = np.linspace(0,-10)
y = np.cos(x)


# Plotting 
def plotting():
    fig = plt.Figure(figsize=(6,4), dpi=100)
    ax = fig.add_subplot()
    ax.plot(x,y, color = 'g')
    canvas = FigureCanvasTkAgg(fig, window) 
    can1 = canvas.get_tk_widget()
    print(can1)
    can1.place(height=380,x=375,y=112) #pack(anchor=N,expand=True)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.grid(color='black',linewidth=0.1)

def clearfunc(obj):
    return 0

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
f_of_x = func.get()
place_holder(func,"Enter a function eg: x^2")
func.pack(anchor=NW,padx=10,pady=5)

# Label for minimum value of x & its textbox
l2 = Label(window,text="minimum value of x") 
l2.pack(anchor=NW,padx=5,pady=5)
minX = Entry(window, width= 30, borderwidth=1)
# minValue = int(minX.get())
place_holder(minX,"Enter a number eg: 10")
minX.pack(anchor=NW,padx=10,pady=5)

# Label for maximum value of x & its textbox
l3 = Label(window,text="maximum value of x")
l3.pack(anchor=NW,padx=5,pady=5)
maxX = Entry(window, width= 30, borderwidth=1)
# maxValue = int(maxX.get())
place_holder(maxX,"Enter a number eg: 10")
maxX.pack(anchor=NW,padx=10,pady=5)

# Clear Button
clBtn = Button(window, text="Clear",command = clearfunc,bg="#DB524B",width=8)
clBtn.pack(side=LEFT,padx=50)

# Plot Button
plBtn = Button(window, text="Plot",command = plotting,bg="#7bd500",width=15)
plBtn.pack(side=LEFT,padx=15)

# vertical separator
ttk.Separator(window, orient='vertical').place(x=350,y=305,anchor = CENTER,height=380)

# assertions
# if(minValue > maxValue):
#     print("error")


window.mainloop()

