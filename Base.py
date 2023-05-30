#IMPORTS
import pygame
import sys

#INITIALIZE PYGAME
pygame.init()

#SURFACE VARIABLES
surfaceWidth = 1500
surfaceHeight = 900

#COLOUR VARIABLES
BLACK = (0,0,0)

#GAME VARIABLES
gameLoop = True

#INITIALIZE GAME WINDOW
surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption("IMFJ2 Project")

#INITIALIZE CLOCK
clock = pygame.time.Clock()

#GAME LOOP
while gameLoop:
    
    #HANDLE EVENTS
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #HANDLE INPUTS
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    #FILL SCREEN WITH BLACK
    surface.fill(BLACK)

    #FLIP THE DISPLAY
    pygame.display.flip()

    #LOCK THE FRAMERATE TO 60
    clock.tick(60)
