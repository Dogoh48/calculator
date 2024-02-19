"""
Module containing the Keypad class.
"""

import tkinter as tk
from tkinter import messagebox

class Keypad(tk.Frame):
    """
    A keypad widget for a calculator application.
    """
    def __init__(self, parent, keynames=[], columns=1, command=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.keynames = keynames
        self.columns = columns
        self.command = command
        self.init_components()

    def init_components(self):
        """
        Initialize the keypad buttons.
        """
        for idx, keyname in enumerate(self.keynames):
            row, col = divmod(idx, self.columns)
            button = tk.Button(self, text=keyname, width=5, height=2, font=('Arial', 12),
                               command=lambda key=keyname: self.handle_click(key))
            button.grid(row=row, column=col, padx=2, pady=2, sticky=tk.NSEW)
            self.rowconfigure(row, weight=1)
            self.columnconfigure(col, weight=1)

    def handle_click(self, key):
        """
        Handle button click events.
        """
        if self.command:
            self.command(key)

    def bind(self, sequence=None, func=None, add=None):
        """Bind an event handler to an event sequence."""
        for button in self.winfo_children():
            button.bind(sequence, func, add)

    def __setitem__(self, key, value):
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for button in self.winfo_children():
            button[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return self.winfo_children()[0][key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons."""
        for button in self.winfo_children():
            button.configure(cnf, **kwargs)

    @property
    def frame(self):
        return super()
