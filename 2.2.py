import tkinter as tk


def update_color(event):

    red = red_scale.get()
    green = green_scale.get()
    blue = blue_scale.get()

    color_canvas.config(bg=rgb_to_hex(red, green, blue))

    color_info.config(text=f"RGB: ({red}, {green}, {blue})\nHex: {rgb_to_hex(red, green, blue)}")


def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


root = tk.Tk()
root.title("Цветовая палитра")


color_canvas = tk.Canvas(root, width=200, height=200, bg="#000000")
color_canvas.pack()


red_scale = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, command=update_color)
red_scale.pack()

green_scale = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, command=update_color)
green_scale.pack()

blue_scale = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, command=update_color)
blue_scale.pack()


color_info = tk.Label(root, text="RGB: (0, 0, 0)\nHex: #000000")
color_info.pack()


root.mainloop()