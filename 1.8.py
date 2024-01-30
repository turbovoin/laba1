import tkinter as tk

def update_text_size():
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        text_field.config(width=width, height=height)
    except ValueError:
        pass

def on_focus_in(event):
    text_field.config(bg='white')

def on_focus_out(event):
    text_field.config(bg='lightgrey')

root = tk.Tk()


width_entry = tk.Entry(root)
width_entry.pack()

height_entry = tk.Entry(root)
height_entry.pack()


update_button = tk.Button(root, text="Update Size", command=update_text_size)
update_button.pack()


text_field = tk.Text(root, bg='lightgrey')
text_field.pack()
text_field.bind('<FocusIn>', on_focus_in)
text_field.bind('<FocusOut>', on_focus_out)


root.bind('<Return>', lambda event: update_text_size())

root.mainloop()