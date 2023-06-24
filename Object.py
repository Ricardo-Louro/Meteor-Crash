class Object:
    position = (0,0)
    colour = (0,0,0)
    radius = 0
    mass = 0
    velocity_x = 0
    velocity_y = 0
    gravity = 9.8
    grounded = False

    def GroundCheck(self, groundHeight):
        if self.position[1] >= (groundHeight - self.radius):
            self.grounded = True
            self.position = (self.position[0], groundHeight - self.radius)
        else:
            self.grounded = False
    
