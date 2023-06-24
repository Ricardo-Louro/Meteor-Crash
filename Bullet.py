from Object import Object

class Bullet(Object):
    colour = (210, 4, 45)
    radius = 5
    velocity_y = -100
    mass = 0.5

    def __init__(self, player):
        super().__init__()
        self.normal_force = self.mass * self.gravity
        self.position = player.position
        self.velocity_x = player.velocity_x
        self.player = player
            
    def Move(self):
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

        self.position = (self.position[0] + self.velocity_x, self.position[1] + self.velocity_y)
