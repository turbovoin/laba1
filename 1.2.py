from tkinter import *
root = Tk()

def red():
    ent.delete(0, END)
    lab1['text'] = "красный"
    ent.insert(0, '#ff0000')
def orange():
    ent.delete(0, END)
    lab1['text'] = "оранжевый"
    ent.insert(END, "#ff7d00")
def yellow():
    ent.delete(0, END)
    lab1['text'] = "желтый"
    ent.insert(0, '#ffff00')
def green():
    ent.delete(0, END)
    lab1['text'] = "зеленый"
    ent.insert(0, '#00ff00')
def blue():
    ent.delete(0, END)
    lab1['text'] = "голубой"
    ent.insert(0, '#007dff')
def blue2():
    ent.delete(0, END)
    lab1['text'] = "синий"
    ent.insert(0, '#0000ff')
def violet():
    ent.delete(0, END)
    lab1['text'] = "фиолетовый"
    ent.insert(0, '#7d00ff')

ent = Entry(width=20)
but1 = Button(bg='red', fg='red', text="#ff0000", command=red)
but2 = Button(bg='orange', fg='orange', text='#ff7d00', command=orange)
but3 = Button(bg='yellow', fg='yellow', text='#ffff00', command=yellow)
but4 = Button(bg='green', fg='green', text='#00ff00', command=green)
but5 = Button(bg='light blue', fg='light blue', text='#007dff', command=blue)
but6 = Button(bg='blue', fg='blue', text='#0000ff', command=blue2)
but7 = Button(bg='dark violet', fg='dark violet', text='#7d00ff', command=violet)
lab1 = Label(width=20, bg='white', fg='black')
lab2 = Label(width=20, bg='white', fg='black')

lab1.pack()
ent.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
but5.pack()
but6.pack()
but7.pack()

l1 = Label(text="Цвета радуги",
font="Bold 35")
l1.config(bd=20, bg='pink')
l1.pack()
root.mainloop()