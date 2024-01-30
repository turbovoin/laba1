import tkinter as tk
from tkinter import simpledialog

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self, width=400, height=400, bg='white')
        self.canvas.grid(row=0, column=0)
        self.add_figure_button = tk.Button(self, text="Добавить фигуру", command=self.add_figure)
        self.add_figure_button.grid(row=1, column=0)

    def add_figure(self):
        AddFigureWindow(self)

class AddFigureWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.x1_entry = tk.Entry(self)
        self.x1_entry.grid(row=0, column=0)
        self.y1_entry = tk.Entry(self)
        self.y1_entry.grid(row=0, column=1)
        self.x2_entry = tk.Entry(self)
        self.x2_entry.grid(row=1, column=0)
        self.y2_entry = tk.Entry(self)
        self.y2_entry.grid(row=1, column=1)
        self.shape_var = tk.StringVar(self, 'rectangle')
        self.rectangle_radio = tk.Radiobutton(self, text="Прямоугольник", variable=self.shape_var, value='rectangle')
        self.rectangle_radio.grid(row=2, column=0)
        self.oval_radio = tk.Radiobutton(self, text="Овал", variable=self.shape_var, value='oval')
        self.oval_radio.grid(row=2, column=1)
        self.draw_button = tk.Button(self, text="Нарисовать", command=self.draw_figure)
        self.draw_button.grid(row=3, column=0, columnspan=2)

    def draw_figure(self):
        x1 = int(self.x1_entry.get())
        y1 = int(self.y1_entry.get())
        x2 = int(self.x2_entry.get())
        y2 = int(self.y2_entry.get())
        shape = self.shape_var.get()
        if shape == 'rectangle':
            self.master.canvas.create_rectangle(x1, y1, x2, y2)
        elif shape == 'oval':
            self.master.canvas.create_oval(x1, y1, x2, y2)
        self.destroy()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
