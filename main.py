import pygame

#initialized pygame.
pygame.init()

#Screen creation.
screen = pygame.display.set_mode((800, 600))

#Title and Icon. Icon image is from Flaticon.com and was created by Pixel perfect.
pygame.display.set_caption("Negative Space")
icon = pygame.image.load('./images/ufo.png')
pygame.display.set_icon(icon)

#Game loop. This portion makes it so that the window stays open until we click the close (x) button.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
