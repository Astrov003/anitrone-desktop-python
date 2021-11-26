import tkinter as tk
from PIL import Image, ImageTk
import time


# --- main ---

root = tk.Tk()

canvas = tk.Canvas(root, width=1080, height=200)
canvas.grid(columnspan=8)

img0 = Image.open('./images/dot.png')
img0 = img0.resize((120, 120))
""" img0_photo = ImageTk.PhotoImage(img0)
img0_label = tk.Label(image=img0_photo)
img0_label.image = img0_photo """

img1 = Image.open('./images/dot_glow.png')
img1 = img1.resize((120, 120))
""" img1_photo = ImageTk.PhotoImage(img1)
img1_label = tk.Label(image=img1_photo)
img1_label.image = img1_photo """


blend_image = Image.blend(img0, img1, 1.0)

blend_image_photo = ImageTk.PhotoImage(blend_image)
blend_img_label = tk.Label(image=blend_image_photo)
blend_img_label.image = blend_image_photo

blend_img_label.grid(column=0, row=0)


root.mainloop()