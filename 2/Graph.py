from matplotlib.figure import Figure
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from Toolbar import Toolbar
import time

matplotlib.use("TkAgg")


class Graph:
    def __init__(self, start_x, end_x, frame=None):
        self.start_x = start_x
        self.end_x = end_x
        self.__frame = frame
        self.__figure = Figure(figsize=(10, 6), dpi=100)

        self.__plot = self.__figure.add_subplot(111)
        self.__plot.grid(True)
        self.__plot.legend(loc='upper left')

        self.__canvas = FigureCanvasTkAgg(self.__figure, master=self.__frame)
        self.__canvas.get_tk_widget().pack()
        self.__canvas.draw()
        self.__canvas.flush_events()

    # Shows function range with red dots
    def show_interval(self):
        self.__plot.plot(self.start_x, 0, 'ro')
        self.__plot(self.end_x, 0, 'ro')

    def show_function(self, x, y, color, label=None):
        self.__plot.plot(x, y, color, label=label)
        self.refresh()

    def refresh(self):
        self.__plot.legend(loc='upper left')
        self.__canvas.draw()

    def set_frame(self, frame):
        self.__frame = frame

    def add_toolbar(self):
        Toolbar(frame=self.__frame, canvas=self.__canvas)

    def get_plot(self):
        return self.__plot

    def get_canvas(self):
        return self.__canvas

    def clear_graph(self):
        self.__plot.clear()