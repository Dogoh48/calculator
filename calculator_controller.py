"""
Module containing the CalculatorController class.
"""

from calculator_view import *

class CalculatorController:
    """
    Controller class for the calculator application.
    """
    def __init__(self):
        self.view = CalculatorView()

    def run(self):
        """
        Start the calculator application.
        """
        self.view.run()
