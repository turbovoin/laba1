from tkinter import *

def on_enter_press(event):
    entered_text = entry.get()
    if entered_text:
        listbox.insert(END, entered_text)
        entry.delete(0, END)
def on_double_click(event):
    selected_item = listbox.get(listbox.curselection())
    entry.delete(0, END)
    entry.insert(0, selected_item)

root = Tk()

entry = Entry(root)
entry.bind("<Return>", on_enter_press)
entry.pack()

listbox = Listbox(root)
listbox.bind("<Double-Button-1>", on_double_click)
listbox.pack()

root.mainloop()