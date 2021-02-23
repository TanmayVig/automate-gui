import tkinter as tk 
from tkinter import ttk 
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
feet_force=0

LARGEFONT =("Verdana", 35) 

time = [1,2,3,4,5,6,7,8]
feet = [5,5,5,5,5.1,5.6,5.7,60]

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)


def live_input(data):
    global feet
    feet.append(data)

# plot
def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    a.clear()
    a.plot(xList, yList)
'''
def plot():
    global feet

    ani = animation.FuncAnimation(f, animate, interval=1000)
    # fig = Figure(figsize=(3,3), dpi=200)
    # plot1 = fig.add_subplot(111)
    # plot1.plot(feet)
    canvas = FigureCanvasTkAgg(f, master=page2)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    toolbar = NavigationToolbar2Tk(canvas,window=page2)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    # canvas = FigureCanvasTkAgg(f, master=page2)
    # canvas.draw()
    # canvas.get_tk_widget().pack()
    # canvas.get_tk_widget().grid(row=2, column=0)
    # canvas.get_tk_widget().pack()

    # toolbar = NavigationToolbar2Tk(canvas,page2)
    # toolbar.update()
    # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    # canvas.get_tk_widget().grid(row=2, column=0)
'''
# to go to page 2 from anywhere 
def goto_page_2():
        page1.forget()
        page2.pack(fill="both", expand=1)
        # page1.forget()

# to go to page 1 from anywhere
def goto_page_1():
        page2.forget()
        page1.pack(fill="both", expand=1)
        # page2.forget()

# changes feetforce according to input
def set_text(num:int):
    global feet_force
    feet_force = feet_force*10 + num
    #feet_force_display.config(text="{}".format(feet_force)) 
    feet_force_display = tk.Label(page1, text=feet_force).grid(row=1,column=3)
    print(feet_force)

# makes feetforce 0
def clear():
    global feet_force
    feet_force=0
    feet_force_display = tk.Label(page1, text="0").grid(row=1,column=3)

# felt usefull might delete later
def show_feet_force():
    global feet_force
    return feet_force

# function to stop the process (on page 2)
def stop():
    '''
    do something
    '''
    root.destroy()

############################## MAIN WINDOW ##########################
root = tk.Tk()
# root.geometry('350x200')
root.title("welding")

page1 = tk.Frame(root)
page2 = tk.Frame(root)

############# PAGE 1 ##############
heading_pg1 = tk.Label(page1,text = "Enter Feet Force:")
heading_pg1.grid(row=1,column=0)
feet_force_display = tk.Label(page1, text=feet_force if feet_force !=0 else "0").grid(row=1,column=3)

# number input buttons
tk.Button(page1, text="1", command=lambda: set_text(1),height=1, width=7).grid(row=5, column=0)
tk.Button(page1, text="2", command=lambda: set_text(2),height=1, width=7).grid(row=5, column=1)
tk.Button(page1, text="3", command=lambda: set_text(3),height=1, width=7).grid(row=5, column=2)
tk.Button(page1, text="4", command=lambda: set_text(4),height=1, width=7).grid(row=6, column=0)
tk.Button(page1, text="5", command=lambda: set_text(5),height=1, width=7).grid(row=6, column=1)
tk.Button(page1, text="6", command=lambda: set_text(6),height=1, width=7).grid(row=6, column=2)
tk.Button(page1, text="7", command=lambda: set_text(7),height=1, width=7).grid(row=7, column=0)
tk.Button(page1, text="8", command=lambda: set_text(8),height=1, width=7).grid(row=7, column=1)
tk.Button(page1, text="9", command=lambda: set_text(9),height=1, width=7).grid(row=7, column=2)
tk.Button(page1, text="0", command=lambda: set_text(0),height=1, width=7).grid(row=8, column=1)

# clear button
tk.Button(page1, text="clear",command = lambda: clear(),height=1, width=7).grid(row=8, column=2)

# button to go to start process and go to page 2
button_to_page2 = tk.Button(page1,text="Start",command=goto_page_2,height=1, width=21)
button_to_page2.grid(row=10, column=1)

page1.pack(expand=1,fill="both")

############# PAGE 2 ################

heading_pg2 = tk.Label(page2,text = "GRAPH")
# heading_pg2.grid(row=0, column=0)
heading_pg2.pack()

# graph vaala part
# plot()

canvas = FigureCanvasTkAgg(f, master=page2)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

toolbar = NavigationToolbar2Tk(canvas,window=page2)
toolbar.update()
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# button to go back to page 1 (might delete later)
# tk.Button(page2, text="page 1",command=goto_page_1,height=1, width=7).grid(row=1,column=0)
tk.Button(page2, text="<- Back",command=goto_page_1,height=1, width=7).pack()

# button to end process
# tk.Button(page2,text="STOP",bg="red",command=stop, height=2, width=7).grid(row=2,column=1)
tk.Button(page2,text="STOP",bg="red",command=stop, height=2, width=7).pack()

page2.forget()
ani = animation.FuncAnimation(f, animate, interval=1000)

root.mainloop()