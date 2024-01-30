import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()
    with open(filepath, 'r') as file:
        content = file.read()
    text_field.delete('1.0', tk.END)
    text_field.insert(tk.END, content)

def save_file():
    filepath = filedialog.asksaveasfilename()
    with open(filepath, 'w') as file:
        file.write(text_field.get('1.0', tk.END))

root = tk.Tk()

open_button = tk.Button(root, text="Открыть", command=open_file)
open_button.pack()

save_button = tk.Button(root, text="Сохранить", command=save_file)
save_button.pack()

text_field = tk.Text(root)
text_field.pack()

root.mainloop()