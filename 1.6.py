import tkinter as tk
from tkinter import Listbox, Button, SINGLE, END

def move_item(source, destination):
    selected_indices = source.curselection()
    if not selected_indices:
        return
    selected_items = [source.get(index) for index in selected_indices]
    for item in selected_items:
        source.delete(source.curselection())
        destination.insert(END, item)

def move_to_cart():
    move_item(product_list, cart_list)

def move_to_products():
    move_item(cart_list, product_list)

root = tk.Tk()

product_list = Listbox(root, selectmode=SINGLE)
product_list.pack(side=tk.LEFT)

cart_list = Listbox(root, selectmode=SINGLE)
cart_list.pack(side=tk.RIGHT)

for product in ["apple", "bananas", "carrot", "bread", "butter", "meat", "potato", "pineapple", "tomato", "milk"]:
    product_list.insert(END, product)

move_to_cart_button = Button(root, text="Move to Cart", command=move_to_cart)
move_to_cart_button.pack()

move_to_products_button = Button(root, text="Move to Products", command=move_to_products)
move_to_products_button.pack()

root.mainloop()