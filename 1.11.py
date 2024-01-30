import tkinter as tk



def draw_shape_window():
    shape_window = tk.Toplevel()
    shape_window.geometry('300x200')
    shape_window.title('Добавить фигуру')


    x1_entry = tk.Entry(shape_window)
    y1_entry = tk.Entry(shape_window)
    x2_entry = tk.Entry(shape_window)
    y2_entry = tk.Entry(shape_window)


    shape_var = tk.IntVar()
    rect_radio = tk.Radiobutton(shape_window, text='Прямоугольник', variable=shape_var, value=1)
    oval_radio = tk.Radiobutton(shape_window, text='Овал', variable=shape_var, value=2)


    draw_button = tk.Button(shape_window, text='Нарисовать', command=lambda: draw_shape())


    x1_entry.grid(row=0, column=1)
    y1_entry.grid(row=1, column=1)
    x2_entry.grid(row=2, column=1)
    y2_entry.grid(row=3, column=1)
    tk.Label(shape_window, text='x1').grid(row=0, column=0)
    tk.Label(shape_window, text='y1').grid(row=1, column=0)
    tk.Label(shape_window, text='x2').grid(row=2, column=0)
    tk.Label(shape_window, text='y2').grid(row=3, column=0)
    rect_radio.grid(row=4, column=0)
    oval_radio.grid(row=5, column=0)
    draw_button.grid(row=6, column=1)


    def draw_shape():
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
        shape_type = shape_var.get()
        if shape_type == 1:
            canvas.create_rectangle(x1, y1, x2, y2)
        elif shape_type == 2:
            canvas.create_oval(x1, y1, x2, y2)
        shape_window.destroy()



root = tk.Tk()
root.geometry('400x400')
root.title('Холст и добавление фигур')


canvas = tk.Canvas(root, width=300, height=300, bg='white')
canvas.pack()


add_shape_button = tk.Button(root, text='Добавить фигуру', command=lambda: draw_shape_window())
add_shape_button.pack()

root.mainloop()