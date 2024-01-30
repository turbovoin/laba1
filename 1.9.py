from tkinter import *
root = Tk()

c = Canvas(root, width=200, height= 200, bg='white')
c.pack()

c.create_rectangle(60, 60, 140, 170, fill='lightgreen', outline='lightgreen')
c.create_polygon(100, 10, 20, 90, 180, 90, fill='dark red', outline='dark red')
c.create_oval(190, 30, 160, 60, fill='yellow', outline='yellow')

x = 0
while x < 200:
    c.create_line(x, 190, x+5, 135, fill='green')
    x +=10
root.mainloop()