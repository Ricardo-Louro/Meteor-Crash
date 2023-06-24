import pygame
from Basic_Functions import *
from Bullet import Bullet
from Exceptions import *

def Main_Menu():
    for event in pygame.event.get():      
        if event.type == pygame.QUIT:
            ExitGame()

        #HANDLE INPUTS WITH KEYS
        elif event.type == pygame.KEYDOWN:
            #IF PRESSED ESCAPE
            if event.key == pygame.K_ESCAPE:
                #QUIT THE GAME
                ExitGame()
            if event.key == pygame.K_SPACE:
                raise Main_Menu_Break
                       
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

            if event.key == pygame.K_w and player.grounded:
                player.velocity_y = -50

            if event.key == pygame.K_SPACE and pygame.time.get_ticks() >= player.lastBulletTime + 500:
                player.bulletList.append(Bullet(player))
                player.lastBulletTime = pygame.time.get_ticks()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            player.force_applied = -player.speed
        if pressed[pygame.K_d]:
            player.force_applied = player.speed
        if not(pressed[pygame.K_d] or pressed[pygame.K_a]):
            player.force_applied = 0

def End_Menu():
    for event in pygame.event.get():      
        if event.type == pygame.QUIT:
            ExitGame()

        #HANDLE INPUTS WITH KEYS
        elif event.type == pygame.KEYDOWN:
            #IF PRESSED ESCAPE
            if event.key == pygame.K_ESCAPE:
                #QUIT THE GAME
                ExitGame()
