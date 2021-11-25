import tkinter as tk
from PIL import Image, ImageTk

# --- functions ---

def switch_img(index):

    if(globals()[f"img{index}_label"].image == images[0]):
        globals()[f"img{index}_label"].configure(image=images[1])
        globals()[f"img{index}_label"].image = images[1]
    elif(globals()[f"img{index}_label"].image == images[1]):
        globals()[f"img{index}_label"].configure(image=images[2])
        globals()[f"img{index}_label"].image = images[2]
    elif(globals()[f"img{index}_label"].image == images[2]):
        globals()[f"img{index}_label"].configure(image=images[3])
        globals()[f"img{index}_label"].image = images[3]
    elif(globals()[f"img{index}_label"].image == images[3]):
        globals()[f"img{index}_label"].configure(image=images[4])
        globals()[f"img{index}_label"].image = images[4]
    elif(globals()[f"img{index}_label"].image == images[4]):
        globals()[f"img{index}_label"].configure(image=images[0])
        globals()[f"img{index}_label"].image = images[0]

def trigger_glow():
    pass

# --- main ---

root = tk.Tk()

canvas = tk.Canvas(root, width=1080, height=200)
canvas.grid(columnspan=8)

img0 = Image.open('./images/dot.png')
img0 = img0.resize((120, 120), Image.ANTIALIAS)
img1 = Image.open('./images/down_full.png')
img1 = img1.resize((120, 120), Image.ANTIALIAS)
img2 = Image.open('./images/down_open.png')
img2 = img2.resize((120, 120), Image.ANTIALIAS)
img3 = Image.open('./images/up_full.png')
img3 = img3.resize((120, 120), Image.ANTIALIAS)
img4 = Image.open('./images/up_open.png')
img4 = img4.resize((120, 120), Image.ANTIALIAS)


images = [
    ImageTk.PhotoImage(img0),
    ImageTk.PhotoImage(img1),
    ImageTk.PhotoImage(img2),
    ImageTk.PhotoImage(img3),
    ImageTk.PhotoImage(img4)
]


img0_label = tk.Label(image=images[0])
img0_label.image = images[0]
img0_label.grid(column=0, row=0)
img0_label.bind('<Button-1>', lambda *_: switch_img('0'))


img1_label = tk.Label(image=images[0])
img1_label.image = images[0]
img1_label.grid(column=1, row=0)
img1_label.bind('<Button-1>', lambda *_: switch_img('1'))
    
img2_label = tk.Label(image=images[0])
img2_label.image = images[0]
img2_label.grid(column=2, row=0)
img2_label.bind('<Button-1>', lambda *_: switch_img('2'))

img3_label = tk.Label(image=images[0])
img3_label.image = images[0]
img3_label.grid(column=3, row=0)
img3_label.bind('<Button-1>', lambda *_: switch_img('3'))

img4_label = tk.Label(image=images[0])
img4_label.image = images[0]
img4_label.grid(column=4, row=0)
img4_label.bind('<Button-1>', lambda *_: switch_img('4'))

img5_label = tk.Label(image=images[0])
img5_label.image = images[0]
img5_label.grid(column=5, row=0)
img5_label.bind('<Button-1>', lambda *_: switch_img('5'))

img6_label = tk.Label(image=images[0])
img6_label.image = images[0]
img6_label.grid(column=6, row=0)
img6_label.bind('<Button-1>', lambda *_: switch_img('6'))

img7_label = tk.Label(image=images[0])
img7_label.image = images[0]
img7_label.grid(column=7, row=0)
img7_label.bind('<Button-1>', lambda *_: switch_img('7'))


root.mainloop()