import math

from Window import Window
import matplotlib
from Graph import Graph
import numpy
from matplotlib import style
from NumericalMethods import NumericalMethod

matplotlib.use("TkAgg")
style.use("ggplot")


def b_part(x):
    return 2 * x * math.sin(x) - ((x / 2) + 2) ** 2


def b_part_derivative(x):
    return 2 * math.sin(x) + 2 * x * math.cos(x) - (x / 2) - 2


def resistance_task(x):
    # return (80 * math.e ** (-((4 * x) / 0.5)) + ((0.5 * 9.8) / x) * (math.e ** (-(4 * x) / 0.5) - 1)) - 10
    return 80 * math.e ** (-8 * x) + (4.9 / x) * (math.e ** (-8 * x) - 1) - 10


# 0.16 * x ** 5 - 1.57 * x ** 4 + 4.38 * x ** 3 - 1.15 * x ** 2 - 6.29 * x + 0.15
function = numpy.poly1d([0.16, -1.57, 4.38, -1.15, -6.29, 0.15])
print(f"Patikrintos x reikšmės {function.roots}")
# function = b_part
# function = resistance_task
# test = function(-0.0001)
# print(test)
derivative = function.deriv()
# derivative = b_part_derivative
# derivative = None

alpha = -10
max_iterations = 1000
precision = 1e20
eps = 1e-4

window = Window(title='Skaitmeniniai algoritmai 12 vr.', size='1250x630')
# function_x_values = numpy.arange(-2, 1, 0.0001)
# function_x_values = numpy.arange(-1, 1, 0.001)  # g(x)
function_x_values = numpy.arange(-3.504, 28.375, 0.001)  # f(x)
function_y_values = [function(x) for x in function_x_values]

graph = Graph(start_x=function_x_values[0], end_x=function_x_values[-1], frame=window.get_graph_frame())
graph.add_toolbar()
# graph.show_function(function_x_values, function_y_values, 'b', 'f(x)')

methods = NumericalMethod(precision, eps, alpha, max_iterations, function,
                          derivative, function_x_values, graph)

window.add_buttons(methods)

window.start()