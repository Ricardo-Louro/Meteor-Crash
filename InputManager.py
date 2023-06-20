import pygame
from Basic_Functions import ExitGame

def Gameplay():
    for event in pygame.event.get():
        
        #HANDLE CLICKING THE X ON THE WINDOW
        if event.type == pygame.QUIT:
            ExitGame()

        #HANDLE INPUTS WITH KEYS
        elif event.type == pygame.KEYDOWN:
            #IF PRESSED ESCAPE
            if event.key == pygame.K_ESCAPE:
                #QUIT THE GAME
                ExitGame()
