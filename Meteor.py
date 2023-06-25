#IMPORT THE RANDOM LIBRARY
import random
#IMPORT THE OBJECT CLASS
from Object import Object

#DECLARE THE METEOR CLASS WHICH INHERITS FROM THE OBJECT CLASS
class Meteor(Object):
    #DECLARE THE METEOR'S COLOUR
    colour = (204,85,0)

    #DECLARE THE CLASS' INITIALIZATION
    def __init__(self, surfaceWidth):
        #CALL THE PARENT CLASS' INITIALIZATION
        super().__init__()
        #SET THE NORMAL FORCE AS THE METEOR'S MASS MULTIPLIED BY THE GRAVITY
        self.normal_force = self.mass * self.gravity
        #SET THE METEOR'S RADIUS AS A RANDOM INT BETWEEN 25 AND 60
        self.radius = random.randint(25,60)
        #SET THE METEOR'S POSITION AS A RANDOM INT BETWEEN THE WIDTH OF THE SCREEN AND A CERTAIN HEIGHT INTERVAL ABOVE THE SCREEN
        self.position = (random.randint(self.radius, surfaceWidth - self.radius), random.randint(-500, -self.radius))

    #DEFINE THE MOVE METHOD     
    def Move(self):
        #SET THEIR VELOCITY IN Y AS A QUARTER OF THE GRAVITY'S VALUE (FOR GAMEPLAY PURPOSES)
        self.velocity_y = self.gravity * 0.25
        #UPDATE THEIR POSITION ACCORDING TO THE VELOCITY IN Y
        self.position = (self.position[0], self.position[1] + self.velocity_y)

    #DEFINE THE BULLET COLLISION HANDLER
    def BulletCollision(self, player):
        #ITERATE THROUGH EVERY BULLET IN THE BULLET LIST
        for bullet in player.bulletList:
            #IF THEIR POSITION'S ARE CLOSE ENOUGH
            if abs(self.position[0] - bullet.position[0]) + abs(self.position[1] - bullet.position[1]) <= self.radius:
                #REMOVE THE BULLET FROM THE BULLET LIST
                player.bulletList.remove(bullet)
                #RETURN TRUE
                return True
        #IF NO BULLET WAS CLOSE ENOUGH, RETURN FALSE
        return False
