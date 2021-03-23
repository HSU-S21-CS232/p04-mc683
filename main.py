import pygame
import pygame_menu
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

enemy_speedoR = 1
enemy_speedoL = -1

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("./images/enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1)
    enemyY_change.append(20)

# Creating Boss
bossImg = pygame.image.load("./images/boss.png")
bossX = 20
bossY = 50
bossX_change = 0.1
bossY_change = -0.1

#Laser from Flaticon.com and was created by Freepik.
#Ready - Can't see the laser yet on screen.
#Fire - laser is currently moving
laserImg = pygame.image.load("./images/laser.png")
laserX = 0
laserY = 480
laserX_change = 0
laserY_change = 3
laser_state = "ready"

#score
score_value = 1
font = pygame.font.SysFont('arial.ttf', 32) #pygame.font.SysFont allows for me to use the font without having to have it in the folder. Google "pygame font".

textX = 10
textY = 10

# Game over text
over_font = pygame.font.SysFont('arial.ttf', 64)

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = font.render("Game Over", True, (255, 255, 255))
    screen.blit(over_text, (355, 250))


#This draws player onto the screen. First argument is the image itself, while the second argument is the coordinates.
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def boss(x, y):
    screen.blit(bossImg, (x, y))

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

is_score_increased = False

#Game loop. As long as running remains true, the game continues.
running = True
while running:

    #RGB values fill the screen.
    screen.fill((0, 0, 128))

    #Background image
    screen.blit(background, (0, 0))


    # This is deciding when to increase the speed.
    if score_value % 5 == 0 and is_score_increased == False:
        enemy_speedoR += 0.1
        enemy_speedoL -= 0.1
        is_score_increased = True

    if score_value % 5 == 3:
        is_score_increased = False



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

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[i] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]



        if enemyX[i] <= 0:
            enemyX_change[i] = enemy_speedoR
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = enemy_speedoL
            enemyY[i] += enemyY_change[i]


        #Collision Part
        collision = isCollision(enemyX[i], enemyY[i], laserX, laserY)
        if collision:
            laserY = 480
            laser_state = "ready"
            score_value += 1

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

    show_score(textX, textY)

    #As it says this updates the screen.
    pygame.display.update()
