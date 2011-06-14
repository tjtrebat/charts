__author__ = 'Tom'

from tkinter import *
from tkinter.ttk import *

class Item:
    def __init__(self, length, label, color):
        self.length = length
        self.label = label
        self.color = color

    def get_extent(self):
        return int((18 / 5) * self.length)

    def __str__(self):
        s = str(self.length) + "\n"
        s += self.label + "\n"
        s += self.color + "\n"
        return s

class Chart:
    def __init__(self, root):
        self.root = root
        self.root.title("Charts")
        self.items = []
        self.notebook = Notebook()
        self.bar_chart = Canvas(self.root)
        self.pie_chart = Canvas(self.root, width=450, height=350)
        self.notebook.add(self.bar_chart, text="Bar Chart")
        self.notebook.add(self.pie_chart, text="Pie Chart")
        self.notebook.pack(expand='yes', fill='both')
        self.add_menu()

    def new_item(self):
        if hasattr(self, "top_level") and self.top_level.winfo_exists():
            self.top_level.focus()
        else:
            self.top_level = Toplevel(self.root, padx=10, pady=10)
        self.top_level.title("Add Item")
        style = Style()
        style.configure("BW.TLabel", padx=20)
        lbl_length = Label(self.top_level, text="Length", style="BW.TLabel")
        lbl_length.grid(row=0, column=0)
        self.length = Spinbox(self.top_level, from_=0, to=100, width=4)
        self.length.grid(row=0, column=1, sticky="w")
        self.label = StringVar()
        lbl_label = Label(self.top_level, text="Label", style="BW.TLabel")
        lbl_label.grid(row=1, column=0)
        Entry(self.top_level, textvariable=self.label).grid(row=1, column=1)
        self.color = StringVar()
        self.color.set("white")
        lbl_color = Label(self.top_level, text="Color", style="BW.TLabel")
        lbl_color.grid(row=2, column=0)
        OptionMenu(self.top_level, self.color, "", "white", "black", "red",
                   "orange", "yellow", "green", "blue", "purple").grid(row=2, column=1, sticky="w")
        add_button = Button(self.top_level, text="Add")
        add_button.bind("<Button-1>", self.add_item)
        add_button.grid(row=3, column=1, pady=10)

    def add_item(self, event):
        item = Item(int(self.length.get()), self.label.get(), self.color.get())
        self.bar_chart.create_rectangle(10, 20 + 30 * len(self.items), 4 * (10 + item.length),
                                     30 + 30 * len(self.items), fill=item.color)
        self.bar_chart.create_text(10, 10 + 30 * len(self.items), text=item.label, anchor="w")
        xy = 90, 20, 370, 300
        start = sum([i.get_extent() for i in self.items])
        extent = item.get_extent()
        print(str(start) + " " + str(extent))
        if extent == 360:
            self.pie_chart.create_oval(xy, fill=item.color)
        else:
            self.pie_chart.create_arc(xy, start=start, extent=extent, fill=item.color)
        self.items.append(item)
        event.widget.master.destroy()

    def add_menu(self):
        menu = Menu(self.root)
        self.file_menu = Menu(menu, tearoff=0)
        self.file_menu.add_command(label="Add Item", command=self.new_item)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=quit)
        menu.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=menu)

if __name__ == "__main__":
    root = Tk()
    Chart(root)
    root.mainloop()