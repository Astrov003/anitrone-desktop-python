import pygame, sys
from pygame.locals import *


# --- functions ---

def switch_image():
    pass


def trigger_glow():
    pass


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


rect=img0.get_rect()
print(rect)

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

    display_surface.blit(img0, (0, 0))
    display_surface.blit(img0, (100, 0))
    display_surface.blit(img0, (200, 0))
    display_surface.blit(img0, (300, 0))
    display_surface.blit(img0, (400, 0))
    display_surface.blit(img0, (500, 0))
    display_surface.blit(img0, (600, 0))
    display_surface.blit(img0, (700, 0))

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
    if transition == "fadein":
        i+=5
    if transition == "fadeout":
        i-=5

    #x=0
    #y=0
    """ 
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        print("click")
        pos = pygame.mouse.get_pos()
        print(x, y)
        if img0.get_rect().collidepoint(pos):
            print("click") """
  
    pos = pygame.mouse.get_pos()
    pressed1 = pygame.mouse.get_pressed()[0]

    if img0.get_rect().collidepoint(pos) and pressed1:
        print("You have opened a chest!")
        display_surface.blit(img1, (0, 0))

    pygame.display.update() 