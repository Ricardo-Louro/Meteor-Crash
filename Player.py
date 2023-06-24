import pygame
from Object import Object

class Player(Object):
    position = (50,50)
    moveSpeed = 10
    colour = (102,255,102)
    radius = 20
    mass = 5
    speed = 3000

    force_applied = 0

    time = 1/60

    def __init__(self):
        super().__init__()
        self.normal_force = self.mass * self.gravity
        
            
    def Move(self):
        if(self.grounded):

            net_force = 0
            coefficient_of_static_friction=0.2
            coefficient_of_kinetic_friction = 0.05

            #STATIC FRICTION
            if self.velocity_x == 0:
                friction = coefficient_of_static_friction * self.normal_force
            #KINETIC FRICTION
            else:
                friction = coefficient_of_kinetic_friction * self.normal_force

            if self.force_applied > 0:                    
                net_force = self.force_applied - friction
            elif self.force_applied < 0:
                net_force = self.force_applied + friction


            acceleration = net_force / self.mass
            self.velocity_x = acceleration * self.time

        else:
            #DRAG
            if self.velocity_x != 0:
                surface_area = self.radius/4
                velocity_squared = self.velocity_x ** 2
                drag_force = 0.5 * self.drag_coefficient * self.air_density * velocity_squared * surface_area
                acceleration = -drag_force / self.mass
                if (self.velocity_x > 0):
                    self.velocity_x += acceleration * self.time
                elif (self.velocity_x < 0):
                    self.velocity_x -= acceleration * self.time

            #FREE FALL
            if(self.velocity_y < self.gravity):
                self.velocity_y += self.gravity
            else:
                self.velocity_y = self.gravity

        #UPDATE POSITION
        self.position = (self.position[0] + self.velocity_x, self.position[1] + self.velocity_y)

    def Draw(self, surface):
        pygame.draw.circle(surface, self.colour, self.position, self.radius)
