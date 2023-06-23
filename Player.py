import pygame

class Player:
    position = (50,50)
    moveSpeed = 10
    colour = (102,255,102)
    radius = 20

    def Move(self, direction):
        if direction == "left":
            moveSpeed = -self.moveSpeed
        else:
            moveSpeed = self.moveSpeed
        
        self.position = (self.position[0] + moveSpeed, self.position[1])

    def Draw(self, surface):
        pygame.draw.circle(surface, self.colour, self.position, self.radius)
