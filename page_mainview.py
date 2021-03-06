import tkinter as tk

from page_one import Page1
from page_two import Page2
from page_three import Page3

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        
        buttomframe = tk.Frame(self)
        container = tk.Frame(self)
        buttomframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        
        b1 = tk.Button(buttomframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttomframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttomframe, text="Page 3", command=p3.lift)
        
        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        
        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()