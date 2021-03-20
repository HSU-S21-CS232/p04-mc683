import pygame

#initialized pygame.
pygame.init()

#Screen creation.
screen = pygame.display.set_mode((800, 600))

#Title and Icon. Icon image is from Flaticon.com and was created by Pixel perfect.
pygame.display.set_caption("Negative Space")
icon = pygame.image.load('./images/ufo.png')
pygame.display.set_icon(icon)

#Player. player.png is from Flaticon.com and was created by Freepik.
playerImg = pygame.image.load("./images/player.png")
playerX = 370
playerY = 480


#This draws player onto the screen. First argument is the image itself, while the second argument is the coordinates.
def player(x, y):
    screen.blit(playerImg, (x, y))

#Game loop. As long as running remains true, the game continues.
running = True
while running:

    #RGB values fill the screen.
    screen.fill((0, 0, 128))
    playerX += .1

    #This checks for pygame events, such as clicking the close(x) button, and will change running to false to end the program.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    #Make sure that the player is called after the screen is created, not before. This is the default starting spot.
    player(playerX, playerY)


    #As it says this updates the screen.
    pygame.display.update()
