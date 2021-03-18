import pygame

#initialized pygame.
pygame.init()

#Screen creation.
screen = pygame.display.set_mode((800, 600))

#Title and Icon. Icon image is from Flaticon.com and was created by Pixel perfect.
pygame.display.set_caption("Negative Space")
icon = pygame.image.load('./images/ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("./images/player.png")
playerX = 370
playerY = 480


#This draws player onto the screen. First argument is the image itself, while the second argument is the coordinates.
def player():
    screen.blit(playerImg, (playerX, playerY))

#Game loop. This portion makes it so that the window stays open until we click the close (x) button.
running = True
while running:

    #RGB values fill the screen.
    screen.fill((0, 0, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    #Make sure that the player is called after the screen is created, not before.
    player()


    #As it says this updates the screen.
    pygame.display.update()
