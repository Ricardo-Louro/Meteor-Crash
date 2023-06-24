#IMPORTS
import pygame
import InputManager

from Player import Player


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

#GAME LOOP
while gameLoop: 
    #HANDLE EVENTS
    InputManager.Gameplay(player)

    player.GroundCheck(surfaceHeight)
    player.Move()

    #FILL SCREEN WITH BLACK
    surface.fill(BLACK)
    player.Draw(surface)

    #FLIP THE DISPLAY
    pygame.display.flip()

    #LOCK THE FRAMERATE TO 60
    clock.tick(60)
