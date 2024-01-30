import tkinter as tk
from random import randint

def move_button():

    window_width = root.winfo_width()
    window_height = root.winfo_height()


    new_x = randint(0, window_width - button.winfo_reqwidth())
    new_y = randint(0, window_height - button.winfo_reqheight())


    button.place(x=new_x, y=new_y)


root = tk.Tk()
root.geometry("800x600")


img = tk.PhotoImage(file='thinking.gif')


button = tk.Button(root, image=img, command=move_button)
button.image = img


button.place(x=root.winfo_width() // 2, y=root.winfo_height() // 2)

root.mainloop()
