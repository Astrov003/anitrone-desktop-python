# import pygame module in this program
import pygame
  
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
X = 1080
Y = 200
  
display_surface = pygame.display.set_mode((X, Y ))

pygame.display.set_caption('Anitrone')
  
# create a surface object, image is drawn on it.
image = pygame.image.load('./images/dot.png')
image = pygame.transform.scale(image, (120, 120))

image2 = pygame.image.load('./images/dot_glow.png')
image2 = pygame.transform.scale(image2, (120, 120))
image2=image2.convert_alpha()
rect2=image2.get_rect()

i=1
# infinite loop
while True :
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()

    display_surface.fill(black)
  
    display_surface.blit(image, (0, 0))

    image2.set_alpha(i)
    display_surface.blit(image2, rect2)
    pygame.time.delay(1)
    
    if i==1:
        transition = "fadein"
    if i==255:
        transition = "fadeout"
    if transition == "fadein":
        i+=1
    if transition == "fadeout":
        i-=1
  
    pygame.display.update() 