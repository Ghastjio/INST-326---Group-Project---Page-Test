import tkinter as tk

from page import Page


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is Page 3")
        label.pack(side="top", fill="both", expand=True)