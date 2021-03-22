import pygame
import math
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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("./images/enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.2)
    enemyY_change.append(10)



#Laser from Flaticon.com and was created by Freepik.
#Ready - Can't see the laser yet on screen.
#Fire - laser is currently moving
laserImg = pygame.image.load("./images/laser.png")
laserX = 0
laserY = 480
laserX_change = 0
laserY_change = 1
laser_state = "ready"

score = 0

#This draws player onto the screen. First argument is the image itself, while the second argument is the coordinates.
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_laser(x, y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserImg, (x + 16, y + 10)) #This draws the laser on screen.

def isCollision(enemyX, enemyY, laserX, laserY):
    distance = math.sqrt((math.pow(enemyX - laserX, 2)) + ( math.pow(enemyY - laserY, 2)))
    if distance < 27:
        return True
    else:
        return False

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
            playerX_change = -0.5
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.5
        if event.key == pygame.K_UP:
            if laser_state is "ready":
                #Gets the current x coordinate of ship.
                laserX = playerX
                fire_laser(laserX, laserY)

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
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.2
            enemyY[i] += enemyY_change[i]

        #Collision Part
        collision = isCollision(enemyX[i], enemyY[i], laserX, laserY)
        if collision:
            laserY = 480
            laser_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)


    #Laser Movement
    if laserY <= 0:
        laserY = 480
        laser_state = "ready"
    if laser_state is "fire":
        fire_laser(laserX, laserY)
        laserY -= laserY_change





    player(playerX, playerY)



    #As it says this updates the screen.
    pygame.display.update()
