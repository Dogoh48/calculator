"""
Module containing the CalculatorModel class.
"""

from math import *

class CalculatorModel:
    """
    A model class for a calculator application.
    """
    def __init__(self):
        self.history = []

    def calculate(self, expression):
        """
        Calculate the result of the given expression.
        """
        try:
            expression = expression.replace('^', '**')
            result = eval(expression)
            self.history.append((expression, result))
            return result
        except Exception as e:
            return None

    def get_history(self):
        """
        Get the calculation history.
        """
        return self.history
