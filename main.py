import pygame
import random

#initialized pygame.
pygame.init()

#Screen creation.
screen = pygame.display.set_mode((800, 600))

#Screen Background. Background image from freepik.com
background = pygame.image.load("./images/background.jpg")

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


#Enemy from Flaticon.com and was created by Freepik.
enemyImg = pygame.image.load("./images/enemy.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 10


#Laser from Flaticon.com and was created by Freepik.
#Ready - Can't see the laser yet on screen.
#Fire - laser is currently moving
laserImg = pygame.image.load("./images/laser.png")
laserX = 0
laserY = 480
laserX_change = 0
laserY_change = 10
laser_state = "ready"


#This draws player onto the screen. First argument is the image itself, while the second argument is the coordinates.
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_laser(x, y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserImg, (x + 16, y + 10)) #This draws the laser on screen.

#Game loop. As long as running remains true, the game continues.
running = True
while running:

    #RGB values fill the screen.
    screen.fill((0, 0, 128))

    #Background image
    screen.blit(background, (0, 0))





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
            fire_laser(playerX, laserY)
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0



    #Make sure that the player is called after the screen is created, not before. This is the default starting spot.
    playerX += playerX_change

    #Checking for boundary of spaceship.
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    playerY += playerY_change

    #Checking for boundary of enemyy.
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

    #Laser Movement
    if laser_state is "fire":
        fire_laser(playerX, laserY)
        laserY -= laserY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)


    #As it says this updates the screen.
    pygame.display.update()
