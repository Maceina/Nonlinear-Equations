class FunctionScanner:
    @staticmethod
    def scan(f, start_x, end_x):
        step = (end_x - start_x) / 40
        x = start_x
        intervals = []

        while x < end_x:
            x_next = x + step
            if (f(x) > 0 > f(x_next)) or (f(x_next) > 0 > f(x)):
                intervals.append([x, x_next])

            x = x_next

        return intervals