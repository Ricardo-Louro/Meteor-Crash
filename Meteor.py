import random
from Object import Object

class Meteor(Object):
    colour = (204,85,0)

    def __init__(self, surfaceWidth):
        super().__init__()
        self.normal_force = self.mass * self.gravity
        self.radius = random.randint(25,60)
        self.position = (random.randint(self.radius, surfaceWidth - self.radius), random.randint(-200, -self.radius))
            
    def Move(self):
        self.velocity_y = self.gravity * 0.25
        self.position = (self.position[0], self.position[1] + self.velocity_y)

    def BulletCollision(self, player):
        for bullet in player.bulletList:
            if abs(self.position[0] - bullet.position[0]) + abs(self.position[1] - bullet.position[1]) < self.radius:
                player.bulletList.remove(bullet)
                return True
        return False
