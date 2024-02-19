"""
Module containing the CalculatorView class.
"""

from calculator_model import *
from keypad import *

class CalculatorView(tk.Tk):
    """
    A view class for a calculator application.
    """
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.model = CalculatorModel()
        self.init_components()

    def init_components(self):
        """
        Initialize the GUI components.
        """
        self.display_var = tk.StringVar()
        self.display = tk.Entry(self, textvariable=self.display_var, font=('Arial', 14),
                                justify='right', state='readonly', bg='white', fg='black')
        self.display.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.BOTH)

        self.history_text = tk.Text(self, height=5, font=('Arial', 10))
        self.history_text.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.BOTH)

        keypad_frame = self.make_keypad()
        keypad_frame.pack(side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.BOTH)

    def make_keypad(self) -> tk.Frame:
        """
        Create and return a keypad frame.
        """
        keys = ['*', '(', ')', 'DEL', 'CLR', '/','7','8','9','sqrt', '+', '4', '5', '6',
                'exp', '-', '1', '2', '3', 'abs', '^', '%', 'ln', 'log2', 'log10', '=']
        keypad_frame = tk.Frame(self)
        keypad = Keypad(keypad_frame, keynames=keys, columns=5, command=self.update_display)
        keypad.pack(fill=tk.BOTH, expand=True)
        return keypad_frame

    def update_display(self, value):
        """
        Update the display based on the button click.
        """
        current_text = self.display_var.get()
        if value == 'DEL':
            self.display_var.set(current_text[:-1])
        elif value == 'CLR':
            self.display_var.set('')
        elif value == '=':
            expression = self.display_var.get()
            result = self.model.calculate(expression)
            if result is not None:
                self.display_var.set(str(result))
                self.update_history(expression, result)
            else:
                messagebox.showerror("Error", "Invalid expression")
        else:
            self.display_var.set(current_text + value)

    def update_history(self, expression, result):
        """
        Update the calculation history.
        """
        self.history_text.insert(tk.END, f"{expression} = {result}\n")
        self.history_text.see(tk.END)

    def run(self):
        """
        Start the GUI event loop.
        """
        self.mainloop()
