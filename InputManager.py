import pygame
from Basic_Functions import ExitGame

def Gameplay(player):
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


        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            player.Move("up")
        if pressed[pygame.K_s]:
            player.Move("down")
