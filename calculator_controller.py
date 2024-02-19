from calculator_view import *

class CalculatorController:
    def __init__(self):
        self.view = CalculatorView()

    def run(self):
        self.view.run()