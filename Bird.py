

class Bird:

    def __init__(self, screen_dim):
        #starting position
        self.screen_dim = screen_dim
        self.radius = 15
        self.x = screen_dim[1] // 2   
        self.y = screen_dim[1] // 2  
        self.vx = 0
        self.vy = 0
        self.ay = .3
        self.flapVel = -6

    def update(self, flapped=False):
        if flapped:
            self.vy = self.flapVel
        self.vy += self.ay
        self.y += self.vy + 0.5*self.ay

        screen_width = self.screen_dim[1]
        if self.y + self.radius > screen_width: self.y = screen_width - self.radius
        if self.y - self.radius < 0: self.y = self.radius
