import pygame, sys
from pygame.locals import *

# --- main ---

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
X = 820
Y = 120
  
display_surface = pygame.display.set_mode((X, Y ))

pygame.display.set_caption('Anitrone')
  
# create a surface object, image is drawn on it.
img0 = pygame.image.load('./images/dot.png')
img0 = pygame.transform.scale(img0, (120, 120))
img1 = pygame.image.load('./images/down_full.png')
img1 = pygame.transform.scale(img1, (120, 120))
img2 = pygame.image.load('./images/down_open.png')
img2 = pygame.transform.scale(img2, (120, 120))
img3 = pygame.image.load('./images/up_full.png')
img3 = pygame.transform.scale(img3, (120, 120))
img4 = pygame.image.load('./images/up_open.png')
img4 = pygame.transform.scale(img4, (120, 120))

btn0 = img0
btn1 = img0
btn2 = img0
btn3 = img0
btn4 = img0
btn5 = img0
btn6 = img0
btn7 = img0

def image_switcher0():
    global btn0
    if btn0 == img0:
        btn0 = img1
    elif btn0 == img1:
        btn0 = img2
    elif btn0 == img2:
        btn0 = img3
    elif btn0 == img3:
        btn0 = img4
    elif btn0 == img4:
        btn0 = img0

def image_switcher1():
    global btn1
    if btn1 == img0:
        btn1 = img1
    elif btn1 == img1:
        btn1 = img2
    elif btn1 == img2:
        btn1 = img3
    elif btn1 == img3:
        btn1 = img4
    elif btn1 == img4:
        btn1 = img0

def image_switcher2():
    global btn2
    if btn2 == img0:
        btn2 = img1
    elif btn2 == img1:
        btn2 = img2
    elif btn2 == img2:
        btn2 = img3
    elif btn2 == img3:
        btn2 = img4
    elif btn2 == img4:
        btn2 = img0

def image_switcher3():
    global btn3
    if btn3 == img0:
        btn3 = img1
    elif btn3 == img1:
        btn3 = img2
    elif btn3 == img2:
        btn3 = img3
    elif btn3 == img3:
        btn3 = img4
    elif btn3 == img4:
        btn3 = img0

def image_switcher4():
    global btn4
    if btn4 == img0:
        btn4 = img1
    elif btn4 == img1:
        btn4 = img2
    elif btn4 == img2:
        btn4 = img3
    elif btn4 == img3:
        btn4 = img4
    elif btn4 == img4:
        btn4 = img0

def image_switcher5():
    global btn5
    if btn5 == img0:
        btn5 = img1
    elif btn5 == img1:
        btn5 = img2
    elif btn5 == img2:
        btn5 = img3
    elif btn5 == img3:
        btn5 = img4
    elif btn5 == img4:
        btn5 = img0

def image_switcher6():
    global btn6
    if btn6 == img0:
        btn6 = img1
    elif btn6 == img1:
        btn6 = img2
    elif btn6 == img2:
        btn6 = img3
    elif btn6 == img3:
        btn6 = img4
    elif btn6 == img4:
        btn6 = img0

def image_switcher7():
    global btn7
    if btn7 == img0:
        btn7 = img1
    elif btn7 == img1:
        btn7 = img2
    elif btn7 == img2:
        btn7 = img3
    elif btn7 == img3:
        btn7 = img4
    elif btn7 == img4:
        btn7 = img0


img_glow0 = pygame.image.load('./images/dot_glow.png')
img_glow0 = pygame.transform.scale(img_glow0, (120, 120))
img_glow0 = img_glow0.convert_alpha()
img_glow1 = pygame.image.load('./images/down_full_glow.png')
img_glow1 = pygame.transform.scale(img_glow1, (120, 120))
img_glow1 = img_glow1.convert_alpha()
img_glow2 = pygame.image.load('./images/down_open_glow.png')
img_glow2 = pygame.transform.scale(img_glow2, (120, 120))
img_glow2 = img_glow2.convert_alpha()
img_glow3 = pygame.image.load('./images/up_full_glow.png')
img_glow3 = pygame.transform.scale(img_glow3, (120, 120))
img_glow3 = img_glow3.convert_alpha()
img_glow4 = pygame.image.load('./images/up_open_glow.png')
img_glow4 = pygame.transform.scale(img_glow4, (120, 120))
img_glow4 = img_glow4.convert_alpha()

i=0
# infinite loop
while True :
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()

    display_surface.fill(black)
    
    display_surface.blit(btn0, (0, 0))
    display_surface.blit(btn1, (100, 0))
    display_surface.blit(btn2, (200, 0))
    display_surface.blit(btn3, (300, 0))
    display_surface.blit(btn4, (400, 0))
    display_surface.blit(btn5, (500, 0))
    display_surface.blit(btn6, (600, 0))
    display_surface.blit(btn7, (700, 0))

    pos = pygame.mouse.get_pos()
    pressed1 = pygame.mouse.get_pressed()[0]

    btn_rect0 = btn0.get_rect()
    if btn_rect0.collidepoint(pos) and pressed1:
        pygame.time.delay(100)
        image_switcher0()
    btn_rect0.x = 100
    if btn_rect0.collidepoint(pos) and pressed1:
        pygame.time.delay(100)
        image_switcher1()
    btn_rect0.x = 200
    if btn_rect0.collidepoint(pos) and pressed1:
        pygame.time.delay(100)
        image_switcher2()
    btn_rect0.x = 300
    if btn_rect0.collidepoint(pos) and pressed1:
        pygame.time.delay(100)
        image_switcher3()
    btn_rect0.x = 400
    if btn_rect0.collidepoint(pos) and pressed1:
        pygame.time.delay(100)
        image_switcher4()
    btn_rect0.x = 500
    if btn_rect0.collidepoint(pos) and pressed1:
        pygame.time.delay(100)
        image_switcher5()
    btn_rect0.x = 600
    if btn_rect0.collidepoint(pos) and pressed1:
        pygame.time.delay(100)
        image_switcher6()
    btn_rect0.x = 700
    if btn_rect0.collidepoint(pos) and pressed1:
        pygame.time.delay(100)
        image_switcher7()


    img_glow0.set_alpha(i)
    display_surface.blit(img_glow0, (0, 0))
    display_surface.blit(img_glow0, (100, 0))
    display_surface.blit(img_glow0, (200, 0))
    display_surface.blit(img_glow0, (300, 0))
    display_surface.blit(img_glow0, (400, 0))
    display_surface.blit(img_glow0, (500, 0))
    display_surface.blit(img_glow0, (600, 0))
    display_surface.blit(img_glow0, (700, 0))
    pygame.time.delay(10)
    
    if i==0:
        transition = "fadein"
    if i==255:
        transition = "fadeout"
    #if transition == "fadein":
        #i+=5
    if transition == "fadeout":
        i-=5

    pygame.display.update() 