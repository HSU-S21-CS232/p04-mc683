import pygame
import pygame_menu
from pygame_menu import Theme
import math
import random
from pygame import mixer
from game import Game

pygame.init()
screen = pygame.display.set_mode((800, 600))

backgroundImg = pygame_menu.baseimage.BaseImage('./images/background.jpg')

myTheme = Theme(background_color = (0, 0, 0, 0), title_background_color = (4, 47, 126), title_font_shadow = True, widget_padding = 25)
myTheme.background_color = backgroundImg

#background Sound. Music: “Star Way”, from PlayOnLoop.com Licensed under Creative Commons by Attribution 4.0
mixer.music.load('./music/background.wav')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

def set_difficulty():
    pass

def start_game():
    Game()


# Menu stuff from pygame-menu.readthedocs.io/en/4.0.1/
menu = pygame_menu.Menu(500, 500, 'Howdy', theme = myTheme)
menu.add.text_input('Name:', default = 'Mikey')
#menu.add.selector('Difficulty:', [('Hard', 1), ('Easy', 2)], onchange = set_difficulty)
menu.add.button('Play', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
