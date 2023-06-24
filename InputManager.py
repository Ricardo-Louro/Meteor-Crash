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

            if event.key == pygame.K_SPACE and player.grounded:
                player.velocity_y = -50


        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            player.force_applied = -player.speed
        if pressed[pygame.K_d]:
            player.force_applied = player.speed
        if not(pressed[pygame.K_d] or pressed[pygame.K_a]):
            player.force_applied = 0
