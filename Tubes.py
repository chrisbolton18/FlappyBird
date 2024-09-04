import pygame
import numpy as np

class Tubes:

    def __init__(self, screen_dim):
        self.tube_ygap = 150
        self.tube_width = 50
        self.tube_xgap = self.tube_width * 4
        self.x = screen_dim[0] - self.tube_width
        
        # Load tube images
        self.top_tube_image = pygame.image.load("top_tube.png").convert_alpha()
        self.bottom_tube_image = pygame.image.load("bottom_tube.png").convert_alpha()
        
        # Scale images to fit tube width and gap
        self.top_tube_image = pygame.transform.scale(self.top_tube_image, (self.tube_width, screen_dim[1] * 0.75))
        self.bottom_tube_image = pygame.transform.scale(self.bottom_tube_image, (self.tube_width, screen_dim[1] * 0.75))
        
        # Generate random heights for tubes
        self.tube_heights = np.random.randint(low=screen_dim[1]*0.25, high=screen_dim[1]*0.75, size=(200))

    def updateTubePosition(self):
        self.x -= 2
        return self.tube_heights

    def render(self, screen):
        for i, height in enumerate(self.tube_heights):
            x = self.x + i * self.tube_xgap
            y_lower = screen.get_height() - height
            y_upper = 0

            # Render the top tube
            top_tube_rect = pygame.Rect(x, y_upper, self.tube_width, height)
            screen.blit(self.top_tube_image, top_tube_rect)

            # Render the bottom tube
            bottom_tube_rect = pygame.Rect(x, y_lower + self.tube_ygap, self.tube_width, screen.get_height() - y_lower - self.tube_ygap)
            screen.blit(self.bottom_tube_image, bottom_tube_rect)
