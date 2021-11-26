import tkinter as tk
from PIL import Image, ImageTk
import time

# --- functions ---

def switch_img(i):

    if(img_label[i].image == images[0]):
        img_label[i].configure(image=images[1])
        img_label[i].image = images[1]
    elif(img_label[i].image == images[1]):
        img_label[i].configure(image=images[2])
        img_label[i].image = images[2]
    elif(img_label[i].image == images[2]):
        img_label[i].configure(image=images[3])
        img_label[i].image = images[3]
    elif(img_label[i].image == images[3]):
        img_label[i].configure(image=images[4])
        img_label[i].image = images[4]
    elif(img_label[i].image == images[4]):
        img_label[i].configure(image=images[0])
        img_label[i].image = images[0]


alpha = 0.00

def crossfade(img_position, img_type): 
    #if(img_label[img_position].image == images[img_type]):
    global alpha
    while alpha < 1.0:
        new_img = Image.blend(img0, img0_glow, alpha)
        new_img_ph = ImageTk.PhotoImage(new_img)
        new_img_label = tk.Label(image=new_img_ph)
        new_img_label.image = new_img_ph  
        new_img_label.grid(column=img_position, row=0)
        alpha += 0.1
        print("check")
        #root.after(10, crossfade)

img_position = 0

def trigger_glow(tempo):
    print(tempo)
    global img_position
    while img_position < 8:
        print(img_position)
        if(img_label[img_position].image == images[0]):
            crossfade(img_position, 0)
        elif(img_label[img_position].image == images[1]):
            crossfade(img_position, 1)
        elif(img_label[img_position].image == images[2]):
            crossfade(img_position, 2)
        elif(img_label[img_position].image == images[3]):
            crossfade(img_position, 3)
        elif(img_label[img_position].image == images[4]):
            crossfade(img_position, 4)
        img_position+=1
        root.after(1000, trigger_glow)
       

# --- main ---

root = tk.Tk()

canvas = tk.Canvas(root, width=1080, height=200)
canvas.grid(columnspan=8)

img0 = Image.open('./images/dot.png')
img0 = img0.resize((120, 120))
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
img0_glow = img0_glow.resize((120, 120))
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

img_label_glow0 = tk.Label(image=images_glow[0])
img_label_glow0.image = images_glow[0]

img_label = {}

img_label[0] = tk.Label(image=images[0])
img_label[0].image = images[0]
img_label[0].grid(column=0, row=0)
img_label[0].bind('<Button-1>', lambda *_: switch_img(0))

img_label[1] = tk.Label(image=images[0])
img_label[1].image = images[0]
img_label[1].grid(column=1, row=0)
img_label[1].bind('<Button-1>', lambda *_: switch_img(1))
    
img_label[2] = tk.Label(image=images[0])
img_label[2].image = images[0]
img_label[2].grid(column=2, row=0)
img_label[2].bind('<Button-1>', lambda *_: switch_img(2))

img_label[3] = tk.Label(image=images[0])
img_label[3].image = images[0]
img_label[3].grid(column=3, row=0)
img_label[3].bind('<Button-1>', lambda *_: switch_img(3))

img_label[4] = tk.Label(image=images[0])
img_label[4].image = images[0]
img_label[4].grid(column=4, row=0)
img_label[4].bind('<Button-1>', lambda *_: switch_img(4))

img_label[5] = tk.Label(image=images[0])
img_label[5].image = images[0]
img_label[5].grid(column=5, row=0)
img_label[5].bind('<Button-1>', lambda *_: switch_img(5))

img_label[6] = tk.Label(image=images[0])
img_label[6].image = images[0]
img_label[6].grid(column=6, row=0)
img_label[6].bind('<Button-1>', lambda *_: switch_img(6))

img_label[7] = tk.Label(image=images[0])
img_label[7].image = images[0]
img_label[7].grid(column=7, row=0)
img_label[7].bind('<Button-1>', lambda *_: switch_img(7))


root.bind('<Control-q>', lambda *_: trigger_glow(120))
root.bind('<Control-w>', lambda *_: trigger_glow(150))
root.bind('<Control-e>', lambda *_: trigger_glow(180))

root.mainloop()