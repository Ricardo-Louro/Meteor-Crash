#IMPORTS
import pygame
import InputManager
from Exceptions import *

from Player import Player
from Meteor import Meteor
from Bullet import Bullet

#INITIALIZE PYGAME
pygame.init()

#SURFACE VARIABLES
surfaceWidth = 1400
#SET HEIGHT AT 950 INSTEAD OF 1000 TO BETTER FIT THE MONITOR
surfaceHeight = 950

#COLOUR VARIABLES
BLACK = (0,0,0)

#GAME VARIABLES
gameLoop = True

#INITIALIZE GAME WINDOW
surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption("IMFJ2 Project")

#INITIALIZE CLOCK
clock = pygame.time.Clock()

player = Player()

try:
    while True:
        InputManager.Main_Menu()
        surface.fill((255,0,0))
        pygame.display.flip()
        clock.tick(60)
        
except Main_Menu_Break:
    pass
    
#GAME LOOP
while gameLoop: 
    #HANDLE EVENTS
    player.GroundCheck(surfaceHeight)
    InputManager.Gameplay(player)
    player.Move()
    for bullet in player.bulletList:
        bullet.Move()

    #FILL SCREEN WITH BLACK
    surface.fill(BLACK)
    player.Draw(surface)
    for bullet in player.bulletList:
        bullet.Draw(surface)

    #FLIP THE DISPLAY
    pygame.display.flip()

    #LOCK THE FRAMERATE TO 60
    clock.tick(60)
