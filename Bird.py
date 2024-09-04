import pygame

class Bird:

    def __init__(self, screen_dim):
        # Load the bird image
        self.image = pygame.image.load("birdMidFlap.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))  # Resize if necessary

        # Starting position
        self.screen_dim = screen_dim
        self.radius = 15  # Adjust based on the size of your image
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
        self.y += self.vy + 0.5 * self.ay

        screen_width = self.screen_dim[1]
        if self.y + self.radius > screen_width: self.y = screen_width - self.radius
        if self.y - self.radius < 0: self.y = self.radius

    def render(self, screen):
        # Blit the image onto the screen at the bird's position
        screen.blit(self.image, (self.x - self.image.get_width() // 2, self.y - self.image.get_height() // 2))
