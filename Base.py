#IMPORT LIBRARIES AND RELEVANT CLASSES/FUNCTIONS/EXCEPTIONS
import pygame
import InputManager
from Exceptions import *
from Player import Player
from Meteor import Meteor
from Bullet import Bullet

#INITIALIZE PYGAME
pygame.init()
#INITIALIZE THE TEXT HANDLER WITHIN PYGAME
pygame.font.init()
#LOAD THE MUSIC FILE SO IT STARTS WITHOUT DELAY WHEN CALLED
pygame.mixer.music.load("music.mp3")

#SURFACE VARIABLES
surfaceWidth = 1400
#SET HEIGHT AT 950 INSTEAD OF 1000 TO BETTER FIT THE MONITOR
surfaceHeight = 950

#INITIALIZE COLOUR VARIABLES
BLACK = (10,10,10)

#INITIALIZE GAME WINDOW
surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
#SET THE GAME WINDOW'S CAPTION
pygame.display.set_caption("METEOR CRASH")

#PLAY THE PREVIOUSLY LOADED MUSIC FILE
pygame.mixer.music.play()

#INITIALIZE CLOCK
clock = pygame.time.Clock()

#CREATE NEW OBJECT OF CLASS PLAYER
player = Player(surfaceWidth, surfaceHeight)

#INITIALIZE THE VARIOUS FONTS THAT WILL BE REQUIRED THROUGHOUT THE GAME
titleFont = pygame.font.Font('freesansbold.ttf', 150)
font = pygame.font.Font('freesansbold.ttf', 100)
smallFont = pygame.font.Font('freesansbold.ttf', 30)

#DECLARE THE TEXT MESSAGES THAT WILL APPEAR IN THE MAIN MENU
gameTitle = titleFont.render('METEOR CRASH', True, (204,85,0))
spaceToStart = font.render('Press SPACE to start!', True, (255,210,210))

#INITIALIZE AN EMPTY LIST OF METEORS
meteorList = []

#TRY TO PERFORM THE FOLLOWING OPERATION
try:
    #INITIALIZE A LOOP
    while True:
        #CALL THE MAIN MENU'S INPUT MANAGER
        InputManager.Main_Menu()
        #FILL THE SCREEN WITH A SOLID COLOUR
        surface.fill(BLACK)
        #WRITE THE GAME'S TITLE
        surface.blit(gameTitle, (80, surfaceHeight/2-100))
        #WIRTE THE INSTRUCTION TO PRESS PLAY TO START
        surface.blit(spaceToStart, (180, surfaceHeight/2+100))
        #FLIP THE DISPLAY
        pygame.display.flip()
        #LIMIT THIS LOOP TO 60 FRAMES PER SECOND
        clock.tick(60)

#ONCE IT DETECTS THE MAIN_MENU_BREAK EXCEPTION INSIDE THE TRY     
except Main_Menu_Break:
    #PASS TO THE NEXT PART OF THE CODE
    pass
    
#INITIALIZE GAME LOOP
while True: 

    #WHILE THE LIST OF METEORS CONTAINS LESS THAN 6 OF THEM
    while len(meteorList) < 6:
        #CREATE A NEW METEOR AND APPEND IT TO THE LIST
        meteorList.append(Meteor(surfaceWidth))

    #RUN THE PLAYER'S GROUND CHECK
    player.GroundCheck(surfaceHeight)
    #RUN THE GAMEPLAY'S INPUT MANAGER
    InputManager.Gameplay(player)
    #RUN THE PLAYER'S WALL CHECK
    player.WallCheck(surfaceWidth)

    #UPDATE THE PLAYER'S POSITION
    player.Move()
    #FOR EVERY BULLET INSIDE THE LIST OF BULLETS
    for bullet in player.bulletList:
        #UPDATE THAT BULLET'S POSITION
        bullet.Move()
    #FOR EVERY METEOR INSIDE THE LIST OF METEORS
    for meteor in meteorList:
        #UPDATE THAT METEOR'S POSITION
        meteor.Move()

    #INITIALIZE THE LOOP WHERE THE METEOR LIST WILL BE HANDLED
    while True:
        #INITIALIZE A BOOL AS FALSE
        remove = False
        #INITIALIZE A REFERENCE TO THE METEOR AS NONE
        removalMeteor = None

        #ITERATE THROUGH EVERY METEOR IN THE METEOR LIST
        for meteor in meteorList:
            #CHECK IF THE METEOR IS TOUCHING THE GROUND
            meteor.GroundCheck(surfaceHeight)
            #IF THEY ARE 
            if meteor.grounded == True:
                #DECLARE THE MESSAGE WHICH DISPLAYS THE FINAL SCORE
                finalScore = font.render('FINAL SCORE: ' + str(player.score), True, (220,220,220))
                
                #INITIALIZE THE END MENU LOOP 
                while True:
                    #CALL THE END MENU'S INPUT MANAGER
                    InputManager.End_Menu()
                    #FILL THE SCREEN WITH A SOLID COLOUR
                    surface.fill(BLACK)
                    #DISPLAY THE FINAL SCORE MESSAGE
                    surface.blit(finalScore, (300, surfaceHeight/2-10))
                    #FLIP THE DISPLAY
                    pygame.display.flip()
                    #LIMIT THIS LOOP TO 60 FRAMES PER SECOND
                    clock.tick(60)
                    
            #IF THE METEOR HAS COLLIDED WITH A BULLET
            if meteor.BulletCollision(player):
                #SET THE BOOL AS TRUE
                remove = True
                #SAVE A REFERENCE TO THE RELEVANT METEOR OBJECT
                removalMeteor = meteor
                #INCREMENT THE PLAYER'S SCORE BY 1
                player.score += 1
                #BREAK OUT OF THE FOR LOOP
                break

        #IF THE FOR LOOP HAS ENDED AND THE BOOL IS TRUE
        if remove == True:
            #REMOVE THE RELEVANT METEOR OBJECT FROM THE LIST
            meteorList.remove(removalMeteor)
            #GO BACK TO THE BEGINNING OF THE LOOP AND ITERATE THROUGH THE LIST AGAIN
            pass
        #IF THE FOR LOOP HAS ENDED AND THE BOOL IS NOT TRUE, THEN BREAK THE LOOP
        break       

    #FILL SCREEN WITH BLACK
    surface.fill(BLACK)
    #DRAW THE PLAYER TO THE SCREEN
    player.Draw(surface)
    #ITERATE THROUGH EVERY BULLET IN THE BULLET LIST
    for bullet in player.bulletList:
        #DRAW THE BULLET TO THE SCREEN
        bullet.Draw(surface)
    #ITERATE THROUGH EVERY METEOR IN THE METEOR LIST
    for meteor in meteorList:
        #DRAW THE METEOR TO THE SCREEN
        meteor.Draw(surface)

    #DECLARE THE MESSAGE WHICH SHOWCASES THE CURRENT SCORE
    currentScore = smallFont.render('SCORE: ' + str(player.score), True, (255,210,210))
    #DISPLAY THE CURRENT SCORE MESSAGE
    surface.blit(currentScore, (1200, 20))
    

    #FLIP THE DISPLAY
    pygame.display.flip()
    #LOCK THE FRAMERATE TO 60
    clock.tick(60)
