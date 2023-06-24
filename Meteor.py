from Object import Object

class Meteor(Object):
    colour = (204,85,0)

    def __init__(self, position, radius):
        super().__init__()
        self.normal_force = self.mass * self.gravity
        self.position = position
        self.radius = radius
            
    def Move(self):
        self.velocity_y = self.gravity
        self.position = (self.position[0], self.position[1] + self.velocity_y)
