import tkinter as tk
from PIL import Image, ImageTk

# --- functions ---

def on_click(index):
    print(index)

# --- main ---

root = tk.Tk()

canvas = tk.Canvas(root, width=1080, height=200)
canvas.grid(columnspan=8)

img0 = Image.open('./images/dot.png')
img0 = img0.resize((150, 150), Image.ANTIALIAS)
img0 = ImageTk.PhotoImage(img0)
btn0 = tk.Button(root, image=img0, borderwidth=0, highlightthickness=0,
                 command=lambda: on_click(0))
btn0.grid(column=0, row=0)


img1 = Image.open('./images/dot.png')
img1 = img1.resize((150, 150), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)
img1_label = tk.Label(image=img1)
img1_label.image = img1
img1_label.grid(column=1, row=0)
img1_label.bind('<Button-1>', lambda *_: on_click(1))




root.mainloop()