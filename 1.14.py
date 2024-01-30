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


menu_bar = tk.Menu(root)
root.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)


open_button = tk.Button(root, text="Открыть", command=open_file)
open_button.pack(side=tk.LEFT, padx=(50, 20))

save_button = tk.Button(root, text="Сохранить", command=save_file)
save_button.pack(side=tk.LEFT)


text_field = tk.Text(root)
text_field.pack(padx=20, pady=20)

text_field_menu = tk.Menu(root, tearoff=0)
text_field_menu.add_command(label="Очистить", command=clear_text)

def on_right_click(event):
    try:
        text_field_menu.tk_popup(event.x_root, event.y_root)
    finally:
        text_field_menu.grab_release()

text_field.bind("<Button-3>", on_right_click)

root.mainloop()