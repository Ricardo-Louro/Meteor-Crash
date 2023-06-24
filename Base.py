#IMPORTS
import pygame
import InputManager
from Exceptions import *

from Player import Player
from Meteor import Meteor
from Bullet import Bullet

#INITIALIZE PYGAME
pygame.init()
pygame.font.init()
pygame.mixer.music.load("music.mp3")

#SURFACE VARIABLES
surfaceWidth = 1400
#SET HEIGHT AT 950 INSTEAD OF 1000 TO BETTER FIT THE MONITOR
surfaceHeight = 950

#COLOUR VARIABLES
BLACK = (10,10,10)

#GAME VARIABLES
gameLoop = True

#INITIALIZE GAME WINDOW
surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption("METEOR CRASH")

#INITIALIZE MUSIC
pygame.mixer.music.play()

#INITIALIZE CLOCK
clock = pygame.time.Clock()

player = Player(surfaceWidth, surfaceHeight)

titleFont = pygame.font.Font('freesansbold.ttf', 150)
font = pygame.font.Font('freesansbold.ttf', 100)

gameTitle = titleFont.render('METEOR CRASH', True, (204,85,0))
spaceToStart = font.render('Press SPACE to start!', True, (255,210,210))

meteorList = []

try:
    while True:
        InputManager.Main_Menu()
        surface.fill(BLACK)
        surface.blit(gameTitle, (80, surfaceHeight/2-100))
        surface.blit(spaceToStart, (180, surfaceHeight/2+100))
        pygame.display.flip()
        clock.tick(60)
        
except Main_Menu_Break:
    pass
    
#GAME LOOP
while gameLoop: 
    #HANDLE EVENTS
    while len(meteorList) < 5:
        meteorList.append(Meteor(surfaceWidth))
    
    player.GroundCheck(surfaceHeight)
    InputManager.Gameplay(player)
    player.WallCheck(surfaceWidth)
    player.Move()
    for bullet in player.bulletList:
        bullet.Move()
    for meteor in meteorList:
        meteor.Move()

    while True:
        remove = False
        removalMeteor = None
        
        for meteor in meteorList:
            if meteor.position[1] > surfaceHeight:
                finalScore = font.render('FINAL SCORE: ' + str(player.score), True, (220,220,220))
                while True:
                    InputManager.End_Menu()
                    surface.fill(BLACK)
                    surface.blit(finalScore, (300, surfaceHeight/2-10))
                    pygame.display.flip()
                    clock.tick(60)
                    
                
            if meteor.BulletCollision(player):
                remove = True
                removalMeteor = meteor
                player.score += 1
                break
            
        if remove == True:
            meteorList.remove(removalMeteor)
            pass
        break       

    #FILL SCREEN WITH BLACK
    surface.fill(BLACK)
    player.Draw(surface)
    for bullet in player.bulletList:
        bullet.Draw(surface)
    for meteor in meteorList:
        meteor.Draw(surface)

    #FLIP THE DISPLAY
    pygame.display.flip()

    #LOCK THE FRAMERATE TO 60
    clock.tick(60)
