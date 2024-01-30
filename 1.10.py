from tkinter import *

def move_ball(event):

    x, y = event.x, event.y

    current_coords = c.coords(ball)

    dx = x - current_coords[0]
    dy = y - current_coords[1]

    step_x = dx / 10
    step_y = dy / 10

    for i in range(10):
        c.move(ball, step_x, step_y)
        c.update()
        c.after(100)

root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
ball = c.create_oval(0, 100, 40, 140, fill='green')
c.pack()


c.bind('<Button-1>', move_ball)

root.mainloop()