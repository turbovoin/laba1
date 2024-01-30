import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    try:
        filepath = filedialog.askopenfilename()
        with open(filepath, 'r') as file:
            content = file.read()
        text_field.delete('1.0', tk.END)
        text_field.insert(tk.END, content)
    except Exception as e:
        messagebox.showinfo("Информация", "Файл не загружен")

def save_file():
    try:
        filepath = filedialog.asksaveasfilename()
        with open(filepath, 'w') as file:
            file.write(text_field.get('1.0', tk.END))
    except Exception as e:
        messagebox.showinfo("Информация", "Файл не сохранен")

def clear_text():
    if messagebox.askyesno("Подтверждение", "Вы уверены, что хотите очистить текст?"):
        text_field.delete('1.0', tk.END)

root = tk.Tk()

open_button = tk.Button(root, text="Открыть", command=open_file)
open_button.pack()

save_button = tk.Button(root, text="Сохранить", command=save_file)
save_button.pack()

clear_button = tk.Button(root, text="Очистить", command=clear_text)
clear_button.pack()

text_field = tk.Text(root)
text_field.pack()

root.mainloop()