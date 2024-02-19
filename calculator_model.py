from math import *

class CalculatorModel:
    def __init__(self):
        self.history = []

    def calculate(self, expression):
        try:
            expression = expression.replace('^', '**')
            result = eval(expression)
            self.history.append((expression, result))
            return result
        except Exception as e:
            return None

    def get_history(self):
        return self.history