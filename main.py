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
playerX_change = 0
playerY_change = 0


#This draws player onto the screen. First argument is the image itself, while the second argument is the coordinates.
def player(x, y):
    screen.blit(playerImg, (x, y))

#Game loop. As long as running remains true, the game continues.
running = True
while running:

    #RGB values fill the screen.
    screen.fill((0, 0, 128))





    #This checks for pygame events, such as clicking the close(x) button, and will change running to false to end the program.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #If keystroke pressed check if it is left or right.
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.1
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.1
        if event.key == pygame.K_UP:
            playerY_change = -0.1
        if event.key == pygame.K_DOWN:
            playerY_change = 0.1
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            playerY_change = 0



    #Make sure that the player is called after the screen is created, not before. This is the default starting spot.
    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)


    #As it says this updates the screen.
    pygame.display.update()
