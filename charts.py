__author__ = 'Tom'

from tkinter import *
from tkinter.ttk import *

class Chart:
    def __init__(self, root):
        self.root = root
        self.root.title("Charts")
        self.add_menu()

    def add_item(self):
        self.file_menu.entryconfig(0, state=DISABLED)
        top_level = Toplevel(self.root, padx=10, pady=10)
        top_level.title("Add Item")
        style = Style()
        style.configure("BW.TLabel", padx=20)
        lbl_length = Label(top_level, text="Length", style="BW.TLabel")
        lbl_length.grid(row=0, column=0)
        self.length = Spinbox(top_level, from_=0, to=100, width=4)
        self.length.grid(row=0, column=1, sticky="w")
        self.label = StringVar()
        lbl_label = Label(top_level, text="Label", style="BW.TLabel")
        lbl_label.grid(row=1, column=0)
        Entry(top_level, textvariable=self.label).grid(row=1, column=1)
        self.color = StringVar()
        lbl_color = Label(top_level, text="Color", style="BW.TLabel")
        lbl_color.grid(row=2, column=0)
        Entry(top_level, textvariable=self.color).grid(row=2, column=1)

    def add_menu(self):
        menu = Menu(self.root)
        self.file_menu = Menu(menu, tearoff=0)
        self.file_menu.add_command(label="Add Item", command=self.add_item)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=quit)
        menu.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=menu)

if __name__ == "__main__":
    root = Tk()
    Chart(root)
    root.mainloop()