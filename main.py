from time import sleep
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

def trigger_glow(index): 
    if(globals()[f"img{index}_label"].image == images[0]):
        globals()[f"img{index}_label"].configure(image=images_glow[0])
        globals()[f"img{index}_label"].image = images_glow[0]
    elif(globals()[f"img{index}_label"].image == images[1]):
        globals()[f"img{index}_label"].configure(image=images_glow[1])
        globals()[f"img{index}_label"].image = images_glow[1]
    elif(globals()[f"img{index}_label"].image == images[2]):
        globals()[f"img{index}_label"].configure(image=images[2])
        globals()[f"img{index}_label"].image = images_glow[2]
    elif(globals()[f"img{index}_label"].image == images[3]):
        globals()[f"img{index}_label"].configure(image=images_glow[3])
        globals()[f"img{index}_label"].image = images_glow[3]
    elif(globals()[f"img{index}_label"].image == images[4]):
        globals()[f"img{index}_label"].configure(image=images_glow[4])
        globals()[f"img{index}_label"].image = images_glow[4]
    
       
def play(tempo):
    print(tempo)
    for index in range(8):
        trigger_glow(index)
        print(index)
        sleep(1)

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

img0_glow = Image.open('./images/dot_glow.png')
img0_glow = img0_glow.resize((120, 120), Image.ANTIALIAS)
img1_glow = Image.open('./images/down_full_glow.png')
img1_glow = img1_glow.resize((120, 120), Image.ANTIALIAS)
img2_glow = Image.open('./images/down_open_glow.png')
img2_glow = img2_glow.resize((120, 120), Image.ANTIALIAS)
img3_glow = Image.open('./images/up_full_glow.png')
img3_glow = img3_glow.resize((120, 120), Image.ANTIALIAS)
img4_glow = Image.open('./images/up_open_glow.png')
img4_glow = img4_glow.resize((120, 120), Image.ANTIALIAS)

images_glow = [
    ImageTk.PhotoImage(img0_glow),
    ImageTk.PhotoImage(img1_glow),
    ImageTk.PhotoImage(img2_glow),
    ImageTk.PhotoImage(img3_glow),
    ImageTk.PhotoImage(img4_glow)
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


root.bind('<Control-q>', lambda *_: play(120))
root.bind('<Control-w>', lambda *_: trigger_glow(150))
root.bind('<Control-e>', lambda *_: trigger_glow(180))

root.mainloop()