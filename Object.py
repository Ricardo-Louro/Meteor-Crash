#IMPORT PYGAME
import pygame

#DECLARE THE OBJECT CLASS
class Object:
    
    #SETUP THE VARIABLES WITH DEFAULT VALUES
    position = (0,0)
    colour = (0,0,0)
    radius = 0
    mass = 0
    velocity_x = 0
    velocity_y = 0
    gravity = 9.8
    drag_coefficient = 0.1
    air_density = 1.225
    time = 1/60
    grounded = False

    #DEFINE THE GROUND CHECK METHOD
    def GroundCheck(self, groundHeight):
        #IF THE OBJECT'S IS TOUCHING THE BOTTOM OF THE SCREEN
        if self.position[1] >= (groundHeight - self.radius):
            #SET GROUNDED AS TRUE
            self.grounded = True
            #PLACE IT IN THE CORRECT POSITION
            self.position = (self.position[0], groundHeight - self.radius)
            #REDUCE THEIR VELOCITY IN Y TO 0
            self.velocity_y = 0
            #RETURN TRUE
            return True
        #IF THE OBJECT IS NOT TOUCHING THE BOTTOM OF THE SCREEN
        else:
            #SET GROUNDED AS FALSE
            self.grounded = False
            #RETURN FALSE
            return False

    #DEFINE THE DRAW METHOD
    def Draw(self, surface):
        #DRAW A CIRCLE IN THE OBJECT'S COLOR AT THEIR POSITION AND WITH THEIR SET RADIUS
        pygame.draw.circle(surface, self.colour, self.position, self.radius)
