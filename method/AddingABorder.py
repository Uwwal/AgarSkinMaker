from method.Method import Method
from tkinter import ttk
from tkinter import *


class AddingABorder(Method):
    def __init__(self, language):
        super().__init__(language)
        self.transparent_boolean = BooleanVar(value=False)

    def get_method_detail_weight(self, frame):
        check = ttk.Checkbutton(frame, text=self.language.get_gradient_transparency(),
                                command=lambda: print(self.transparent_boolean.get()), variable=self.transparent_boolean,
                                onvalue=True, offvalue=False
                                )
        check.grid(column=0, row=0, sticky=(N, W, E, S))
