import pygame
from Object import Object

class Player(Object):
    position = (50,50)
    moveSpeed = 10
    colour = (102,255,102)
    radius = 20

    def Move(self, direction):
        self.position = (self.position[0] + self.velocity_x, self.position[1] + self.velocity_x)
        if grounded:
            self.velocity_x *= 0.5

    def Draw(self, surface):
        pygame.draw.circle(surface, self.colour, self.position,

    def GroundCheck(self, groundHeight):
        self.position[0] >= groundHeight - self.radius
            self.grounded = true
        else:
            self.grounded = false

