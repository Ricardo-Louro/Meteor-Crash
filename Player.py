import pygame
from Object import Object

class Player(Object):
    position = (50,50)
    moveSpeed = 10
    colour = (102,255,102)
    radius = 20
    mass = 5

    force_applied = 0

    time = 1/60

    def __init__(self):
        super().__init__()
        self.normal_force = self.mass * self.gravity
        
            
    def Move(self):
        print(self.grounded)
        if(self.grounded):
            self.velocity_y = 0
            coefficient_of_static_friction=0.2
            static_friction = coefficient_of_static_friction * self.normal_force
            net_force = self.force_applied - static_friction
            
            #kinetic friction
            coefficient_of_kinetic_friction = 0.05
            kinetic_friction = coefficient_of_kinetic_friction * self.normal_force
            net_force = self.force_applied - kinetic_friction
            acceleration = net_force / self.mass
            self.velocity_x = acceleration * self.time
        else:
            self.velocity_y = self.gravity
            
        self.position = (self.position[0] + self.velocity_x, self.position[1] + self.velocity_y)

    def Draw(self, surface):
        pygame.draw.circle(surface, self.colour, self.position, self.radius)
