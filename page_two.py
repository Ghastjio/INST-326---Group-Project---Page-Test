import tkinter as tk

from page import Page


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is Page 2")
        label.pack(side="top", fill="both", expand=True)