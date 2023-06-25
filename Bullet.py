#IMPORT THE OBJECT CLASS
from Object import Object

#DECLARE A BULLET CLASS THAT INHERITS FROM OBJECT
class Bullet(Object):
    #DECLARE THIS CLASS' SPECIFIC VARIABLES
    colour = (210, 4, 45)
    radius = 5
    velocity_y = -50
    mass = 1

    #DECLARE THE OBJECT'S INITIALIZATION
    def __init__(self, player):
        #CALL THE PARENT CLASS' (OBJECT) INITIALIZATION
        super().__init__()
        #SET THE NORMAL FORCE AS THE MASS MULTIPLIED BY THE GRAVITY
        self.normal_force = self.mass * self.gravity
        #SET THEIR POSITION AS THE PLAYER'S POSITION
        self.position = player.position
        #SET THEIR VELOCITY IN THE X AXIS AS THE PLAYER'S VELOCITY IN THE X AXIS
        self.velocity_x = player.velocity_x
        #DECLARE A REFERENCE TO THE PLAYER
        self.player = player

    #DECLARE THE MOVE FUNCTION  
    def Move(self):
        #IF THEIR VELOCITY IN THE X AXIS IS DIFFERENT THAN 0
        if self.velocity_x != 0:
            #CALCULARE THE SURFACE AREA
            surface_area = self.radius/4
            #CALCULATE THE SQUARED VELOCITY
            velocity_squared = self.velocity_x ** 2
            #CALCULATE THE DRAG FORCE THAT WILL BE APPLIED TO THE BULLET
            drag_force = 0.5 * self.drag_coefficient * self.air_density * velocity_squared * surface_area
            #SET THE ACCELERATION AS THE NEGATIVE DRAG FORCE DIVIDED BY THE OBJECT'S MASS
            acceleration = -drag_force / self.mass
            #IF THE BULLET IS MOVING RIGHT
            if (self.velocity_x > 0):
                #IMPLEMENT THE DRAG IN THE CORRECT DIRECTION
                self.velocity_x += acceleration * self.time
            #IF THE BULLET IS MOVING LEFT
            elif (self.velocity_x < 0):
                #IMPLEMENT THE DRAG IN THE CORRECT DIRECTION
                self.velocity_x -= acceleration * self.time

        #IF THE BULLET'S VELOCITY IN THE Y AXIS IS LESS THAN THE GRAVITY'S VALUE
        if(self.velocity_y < self.gravity):
            #ADD THE VALUE OF THE GRAVITY (REDUCED BY A QUARTER FOR GAMEPLAY PURPOSES) TO THE BULLET
            self.velocity_y += self.gravity * 0.25
        #IF THE BULLET'S VELOCITY IN THE Y AXIS IS EQUAL OR GREATER THAN THE GRAVITY'S VALUE
        else:
            #SET THE BULLET'S VELOCITY IN THE Y AXIS AS THE GRAVITY'S VALUE
            self.velocity_y = self.gravity

        #UPDATE THE BULLET'S POSITION IN THE X AXIS AND THE Y AXIS
        self.position = (self.position[0] + self.velocity_x, self.position[1] + self.velocity_y)
