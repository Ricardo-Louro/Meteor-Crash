import pygame
from Object import Object

class Player(Object):
    position = (50,50)
    moveSpeed = 10
    colour = (102,255,102)
    radius = 20
    mass = 5

    normal_force = self.mass * gravity 



        self.position = (self.position[0] + self.velocity_x, self.position[1] + self.velocity_x)
        if grounded:
            self.velocity_x *= 0.5

            
    def Move(self, direction):
        coefficient_of_static_friction=0.2
        static_friction = coefficient_of_static_friction * normal_force
        net_force = force_applied - static_friction
        if(net_force>0):
           #kinetic friction
           coefficient_of_kinetic_friction = 0.05
           kinetic_friction = coefficient_of_kinetic_friction * normal_force
           net_force = force_applied - kinetic_friction
           acceleration = net_force / ball_mass
           self.velocity_x = acceleration * t
        else:
            self.velocity_x=0   

    def Draw(self, surface):
        pygame.draw.circle(surface, self.colour, self.position,

    def GroundCheck(self, groundHeight):
        self.position[0] >= groundHeight - self.radius
            self.grounded = true
        else:
            self.grounded = false
