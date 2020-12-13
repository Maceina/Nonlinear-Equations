  
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk, FigureCanvasTkAgg
import tkinter


class Toolbar:
    def __init__(self, frame, canvas):
        # Adds graph's toolbar
        toolbar = tkinter.Frame(master=frame)
        toolbar.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        toolbar.pack()
        toolbar = NavigationToolbar2Tk(canvas, toolbar)
        toolbar.config(background='white')