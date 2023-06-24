import pygame

class Object:
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

    def GroundCheck(self, groundHeight):
        if self.position[1] >= (groundHeight - self.radius):
            self.grounded = True
            self.position = (self.position[0], groundHeight - self.radius)
            self.velocity_y = 0
            return True
        else:
            self.grounded = False
            return False

    def Draw(self, surface):
        pygame.draw.circle(surface, self.colour, self.position, self.radius)
