#IMPORT THE RELEVANT LIBRARIES AND CLASSES/EXCEPTIONS
import pygame
import sys
from Bullet import Bullet
from Exceptions import *

#DECLARE THE INPUT MANAGER FOR THE MAIN MENU
def Main_Menu():
    #ITERATE THROUGH EVERY EVENT IN THE EVENT LIST
    for event in pygame.event.get():
        #IF THE PLAYER HAS CLICKED THE RED X ON THE WINDOW
        if event.type == pygame.QUIT:
            #EXIT THE GAME
            ExitGame()

        #IF THE PLAYER HAS CLICKED A KEY
        elif event.type == pygame.KEYDOWN:
            #IF THEY PRESSED ESCAPE
            if event.key == pygame.K_ESCAPE:
                #QUIT THE GAME
                ExitGame()
            #IF THEY PRESSED SPACE
            if event.key == pygame.K_SPACE:
                #RAISE THE MAIN_MENU_BREAK EXCEPTION
                raise Main_Menu_Break

#DECLARE THE INPUT MANAGER FOR THE GAMEPLAY                  
def Gameplay(player):
    #ITERATE THROUGH EVERY EVENT IN THE EVENT LIST
    for event in pygame.event.get():      
        #IF THE PLAYER HAS CLICKED THE RED X ON THE WINDOW
        if event.type == pygame.QUIT:
            #EXIT THE GAME
            ExitGame()

        #IF THE PLAYER HAS CLICKED A KEY
        elif event.type == pygame.KEYDOWN:
            #IF THEY PRESSED ESCAPE
            if event.key == pygame.K_ESCAPE:
                #QUIT THE GAME
                ExitGame()
            #IF THEY PRESSED W AND THE PLAYER IS GROUNDED
            if event.key == pygame.K_w and player.grounded:
                #THE PLAYER'S VELOCITY IN THE Y AXIS INCREASES IN THE NEGATIVE DIRECTION (PYGAME IS INVERTED IN THE Y AXIS)
                player.velocity_y = -50
            #IF THE PRESSED SPACE AND IT WASN'T WITHIN 500 MS OF FIRING THE LAST BULLET 
            if event.key == pygame.K_SPACE and pygame.time.get_ticks() >= player.lastBulletTime + 500:
                #CREATE A NEW BULLET AND ADD IT TO THE BULLET LIST
                player.bulletList.append(Bullet(player))
                #UPDATE THE TIME FOR THE PLAYER FIRING THE LAST BULLET 
                player.lastBulletTime = pygame.time.get_ticks()


        pressed = pygame.key.get_pressed()        
        #IF THE PLAYER IS HOLDING A
        if pressed[pygame.K_a]:
            #INCREASE THE FORCE APPLIED TO THEM IN THE NEGATIVE DIRECTION
            player.force_applied = -player.speed
        #IF THE PLAYER IS HOLDING D
        if pressed[pygame.K_d]:
            #INCREASE THE FORCE APPLIED TO THEM IN THE POSITIVE DIRECTION
            player.force_applied = player.speed
        #IF NEITHER A NOR D ARE BEING HELD
        if not(pressed[pygame.K_d] or pressed[pygame.K_a]):
            #SET THE FORCE BEING APPLIED TO THE PLAYER AS 0
            player.force_applied = 0

#DECLARE THE INPUT MANAGER FOR THE END MENU
def End_Menu():
    #FOR EVERY EVENT IN THE EVENT LIST
    for event in pygame.event.get():
        #IF THE PLAYER HAS CLICKED THE RED X
        if event.type == pygame.QUIT:
            #EXIT THE GAME
            ExitGame()

        #IF THE PLAYER HAS CLICKED A KEY
        elif event.type == pygame.KEYDOWN:
            #IF THEY PRESSED ESCAPE
            if event.key == pygame.K_ESCAPE:
                #QUIT THE GAME
                ExitGame()

#DECLARE THE FUNCTION THAT EXITS THE GAME
def ExitGame():
    pygame.quit()
    sys.exit()
