from platform import python_branch
from turtle import Screen
import pygame
from sys import exit

from pygame.locals import *
from gameObjects import * # Our own file

import random


# Init pygame
# -----------------
pygame.init()

Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREN_HEIGTH))
background = pygame.image.load('resources/image/background.png').convert()

player_rect = []
# pygame.Rect --> pygame object for storing rectangular coordinates
player_rect.append(pygame.Rect(0, 99, 102, 126)) 
player_rect.append(pygame.Rect(165, 360, 102, 126))
