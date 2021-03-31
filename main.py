import pygame
import pygame_menu
import math
import random
from pygame import mixer
from game import Game

pygame.init()
screen = pygame.display.set_mode((800, 600))

def set_difficulty():
    pass

def start_game():
    Game()

# Menu stuff from pygame-menu.readthedocs.io/en/4.0.1/
menu = pygame_menu.Menu(300, 400, 'Howdy', theme = pygame_menu.themes.THEME_BLUE)
menu.add.text_input('Name:', default = 'Mikey')
menu.add.selector('Difficulty:', [('Hard', 1), ('Easy', 2)], onchange = set_difficulty)
menu.add.button('Play', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
