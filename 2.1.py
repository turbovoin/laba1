import tkinter as tk
from random import choice


phrases_and_colors = [
    ("Красный такой яркий и острый", "red"),
    ("Желтый - это счастливый цвет", "yellow"),
    ("Зеленый цвет радуги", "green"),
    ("Фиолетовый - это красивый цвет", "purple"),
    ("Оранжевый - это яркий и энергичный", "orange")
]

def generate_phrase():

    phrase, color = choice(phrases_and_colors)

    button.config(text=phrase, fg=color)


root = tk.Tk()
root.title("Генератор фраз")


button = tk.Button(root, text="Сгенерировать фразу", command=generate_phrase)
button.pack(pady=20)


root.mainloop()