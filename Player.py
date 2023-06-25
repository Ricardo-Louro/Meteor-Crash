#IMPORT PYGAME
import pygame
#IMPORT THE OBJECT CLASS
from Object import Object

#DECLARE THE PLAYER CLASS WHICH INHERITS FROM OBJECT
class Player(Object):
    #DECLARE THE CLASS SPECIFIC VARIABLES
    moveSpeed = 10
    colour = (102,255,102)
    radius = 20
    mass = 2
    speed = 2000
    score = 0
    force_applied = 0

    #DECLARE THE BULLET LIST
    bulletList = []

    #DECLARE THE PLAYER'S INITIALIZATION
    def __init__(self, surfaceHeight, surfaceWidth):
        #CALL THE PARENT CLASS' INITIALIZATION
        super().__init__()
        #SET THE NORMAL_FORCE AS THE PLAYER'S MASS TIMES THE GRAVITY
        self.normal_force = self.mass * self.gravity
        #SET THE LAST TIME A BULLET WAS FIRED AS THE CURRENT TIME
        self.lastBulletTime = pygame.time.get_ticks()
        #SET THEIR INITIAL POSITION
        self.position = (surfaceWidth/2, surfaceHeight - self.radius)

    #DEFINE THE WALL CHECK METHOD
    def WallCheck(self, surfaceWidth):
        #IF THE PLAYER IS MOVING RIGHT AND THEY'RE TOUCHING THE RIGHT WALL
        if self.position[0] >= surfaceWidth - self.radius and self.force_applied > 0:
            #PLACE THEM IN THE CORRECT POSITION
            self.position = (surfaceWidth - self.radius, self.position[1])
            #REMOVE THE FORCE APPLIED TO IT
            self.force_applied = 0
            
        #IF THE PLAYER IS MOVING LEFT AND THEY'RE TOUCHING THE LEFT WALL    
        elif self.position[0] <= 0 + self.radius and self.force_applied < 0:
            #PLACE THEM IN THE CORRECT POSITION
            self.position = (self.radius, self.position[1])
            #REMOVE THE FORCE APPLIED TO IT
            self.force_applied = 0        

    #DEFINE THE MOVE METHOD 
    def Move(self):
        #IF THE PLAYER IS GROUNDED
        if(self.grounded):
            
            #DECLARE SOME VARIABLE'S VALUES
            net_force = 0
            coefficient_of_static_friction=0.2
            coefficient_of_kinetic_friction = 0.05

            #IF THE PLAYER'S VELOCITY IN X IS 0
            if self.velocity_x == 0:
                #USE THE STATIC FRICTION COEFFICIENT TO CALCULATE THE FRICTION
                friction = coefficient_of_static_friction * self.normal_force
            #IF THE PLAYER'S VELOCITY IN X IS NOT 0
            else:
                #USE THE KINETIC FRICTION COEFFICIENT TO CALCULATE THE FRICTION
                friction = coefficient_of_kinetic_friction * self.normal_force

            #IF THE FORCE IS APPLIED TO THE RIGHT DIRECTION
            if self.force_applied > 0:
                #APPLY THE FRICTION TO THE LEFT DIRECTION
                net_force = self.force_applied - friction
            #IF THE FORCE IS APPLIED TO THE LEFT DIRECTION
            elif self.force_applied < 0:
                #APPLY THE FRICTION TO THE RIGHT DIRECTION
                net_force = self.force_applied + friction

            #SET THE ACCELERATION AS THE NET_FORCE DIVIDED BY THE PLAYER'S MASS
            acceleration = net_force / self.mass
            #SET THE PLAYER'S VELOCITY IN X AS THEIR ACCELERATION MULTIPLIED BY THE TIME OF A FRAME.
            self.velocity_x = acceleration * self.time

        #IF THE PLAYER IS NOT GROUNDED
        else:
            #IF THE PLAYER'S VELOCITY IN X IS NOT 0
            if self.velocity_x != 0:
                #CALCULATE THE SURFACE AREA
                surface_area = self.radius/4
                #CALCULATE THE VELOCITY SQUARED
                velocity_squared = self.velocity_x ** 2
                #CALCULATE THE DRAG FORCE
                drag_force = 0.5 * self.drag_coefficient * self.air_density * velocity_squared * surface_area
                #CALCULATE THE ACCELERATION UTILIZING THE DRAG FORCE
                acceleration = -drag_force / self.mass
                #IF THE PLAYER IS MOVING RIGHT
                if (self.velocity_x > 0):
                    #REMOVE VELOCITY BY APPLYING THE ACCELERATION TO THE LEFT SIDE
                    self.velocity_x += acceleration * self.time
                #IF THE PLAYER IS MOVING LEFT
                elif (self.velocity_x < 0):
                    #REMOVE VELOCITY BY APPLYING THE ACCELERATION TO THE RIGHT SIDE
                    self.velocity_x -= acceleration * self.time

            #IF THE PLAYER'S VELOCITY IN Y IS LESS THAN THE GRAVITY'S VALUE
            if(self.velocity_y < self.gravity):
                #INCREMENT IT BY THE GRAVITY'S VALUE
                self.velocity_y += self.gravity
            #IF THE PLAYER'S VELOCITY IN Y IS EQUAL OR GREATER THAN THE GRAVITY'S VALUE
            else:
                #SET THE PLAYER'S VELOCITY IN Y AS THE GRAVITY'S VALUE
                self.velocity_y = self.gravity

        #UPDATE THE PLAYER'S POSITION DEPENDING ON THEIR VELOCITIES
        self.position = (self.position[0] + self.velocity_x, self.position[1] + self.velocity_y)
