from FunctionScanner import FunctionScanner


class NumericalMethod:
    def __init__(self, precision, eps, alpha, max_iterations, function, derivative,
                 function_x_values, graph):
        self.precision = precision
        self.eps = eps
        self.alpha = alpha
        self.max_iterations = max_iterations
        self.function = function
        self.derivative = derivative
        self.function_x_values = function_x_values
        self.graph = graph

        scanner = FunctionScanner()
        self.intervals = scanner.scan(f=self.function, start_x=self.function_x_values[0],
                                      end_x=self.function_x_values[-1])

    def simple_iteration_method(self):
        self.table_header('Paprastųjų iteracijų metodas')

        self.graph.clear_graph()
        self.graph.show_function(self.function_x_values,
                                 [x + (self.function(x) / self.alpha) for x in self.function_x_values],
                                 'b', 'f(x)')
        self.graph.show_function(self.function_x_values, self.function_x_values, 'r', 'y')
        self.graph.show_function(self.function_x_values[0], 0, color='ro')
        self.graph.show_function(self.function_x_values[-1], 0, color='ro')

        for interval in self.intervals:
            x = interval[0]
            iteration = 0  # Iteration count
            prec = self.precision
            while prec > self.eps and x >= self.function_x_values[0]:
                iteration += 1
                if iteration == self.max_iterations:
                    print("Reached max iterations limit")
                    return

                if x > self.function_x_values[-1]:
                    print('X out of bounds')
                    return

                next_x = (self.function(x) / self.alpha) + x
                self.graph.show_function([x, x, next_x], [x, next_x, next_x], 'g-')

                prec = abs(x - next_x)
                x = next_x
            self.table_content(interval[0], interval[1], prec, iteration, x)

        self.table_footer()

    def scanning_method(self):
        self.table_header('Skenavimo su mažėjančiu žingsniu')

        self.graph.clear_graph()
        self.graph.show_function(self.function_x_values, [self.function(x) for x in self.function_x_values], 'b',
                                 'f(x)')
        self.graph.show_function(self.function_x_values[0], 0, color='ro')
        self.graph.show_function(self.function_x_values[-1], 0, color='ro')

        for interval in self.intervals:
            prec = 0.1
            step = 0.1

            current = interval[0]
            is_positive = self.function(current) > 0
            changed = False
            current_iteration = 0
            iteration_counter = 0

            while prec > self.eps:
                if current_iteration >= self.max_iterations:
                    print("Reached max iterations limit")
                    return
                y = self.function(current)
                if is_positive is not (y > 0):
                    current -= step
                    step /= 2
                    self.graph.show_function(current, 0, color='bo')
                    changed = True
                else:
                    # time.sleep(0.1)
                    if changed is False:
                        self.graph.show_function(current, 0, color='yo')

                    changed = False
                    current += step

                prec = abs(y)
                iteration_counter += 1
                is_positive = y > 0

            self.table_content(interval[0], interval[1], prec, iteration_counter, current)

        self.table_footer()

    def newton_method(self):
        self.table_header('Niutono (liestinių) metodas')

        self.graph.clear_graph()
        self.graph.show_function(self.function_x_values, [self.function(x) for x in self.function_x_values], 'b',
                                 'f(x)')
        self.graph.show_function(self.function_x_values[0], 0, color='ro')
        self.graph.show_function(self.function_x_values[-1], 0, color='ro')

        for interval in self.intervals:

            prec = 0.1
            x = (interval[0] + interval[-1]) / 2
            current_iteration = 0

            while prec > self.eps:
                if current_iteration >= self.max_iterations:
                    print("Reached max iterations limit")
                    return

                next_x = (x - self.function(x) / self.derivative(x))
                prec = abs(next_x - x)

                x = next_x
                current_iteration += 1

            self.table_content(interval[0], interval[1], prec, current_iteration, x)

        self.table_footer()

    @staticmethod
    def table_header(title):
        print('-' * 129)
        print('-' * 45 + '{0:^40}'.format(title) + '-' * 44)
        print('-' * 129)
        print(
            '|                    INTERVALAS                  |          TIKSLUMAS          |   ITERACIJŲ SKAIČIUS  | '
            '       ŠAKNIS          |')
        print('-' * 129)

    @staticmethod
    def table_content(start, end, prec, iteration_counter, root):
        print('|  [{0:^20}, {1:^20}]  |  {2:^25}  |  {3:^19}  |  {4:^20}  |'.format(start, end, prec,
                                                                                    iteration_counter, root))

    @staticmethod
    def table_footer():
        print('-' * 129)