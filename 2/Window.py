import tkinter
# from NumericalMethods import *
from Graph import Graph


class Window:
    def __init__(self, title, size):
        self.__window = tkinter.Tk()
        self.__window.title(title)
        self.__window.geometry(size)
        self.__window.resizable(0, 0)

        self.__graph_frame = tkinter.Frame(self.__window)
        self.__menu_frame = tkinter.Frame(self.__window)

        self.__graph_frame.configure(background='white')
        self.__menu_frame.configure(background='white')

        self.__graph_frame.pack(side='left', expand=True, fill='both')
        self.__menu_frame.pack(side='left', expand=True, fill='both')
        self.__menu_frame.grid_columnconfigure(0, weight=1)

        self.current_page = 0

    def start(self):
        self.__window.mainloop()

    def add_buttons(self, methods):
        tkinter.Button(self.__menu_frame,
                       text="Paprastujų iteracijų metodas",
                       width=25,
                       command=methods.simple_iteration_method).grid(row=0, column=0, sticky="e", pady=(0, 2))

        tkinter.Button(self.__menu_frame,
                       text="Niutono (liestinių) metodas", width=25,
                       command=methods.newton_method).grid(row=1, column=0, sticky="e", pady=2)

        tkinter.Button(self.__menu_frame,
                       text="Skenavimo metodas",
                       width=25,
                       command=methods.scanning_method).grid(row=2, column=0, sticky="e", pady=2)

    def get_graph_frame(self):
        return self.__graph_frame