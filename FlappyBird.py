import pygame
from Tubes import Tubes
from Bird import Bird

pygame.init()
screen_dim = (600, 720)
screen = pygame.display.set_mode(screen_dim)
clock = pygame.time.Clock()
running = True

tubes = Tubes(screen_dim)
bird = Bird(screen_dim)

def renderTubes():
    for i,height in enumerate(heights):
        x = tubes.x - tubes.tube_width + i*tubes.tube_xgap
        y_lower = screen_dim[1] - height
        y_upper = 0
        dy_lower = height
        dy_upper = screen_dim[1] - height - tubes.tube_ygap
        pygame.draw.rect(screen, (0,255,60), pygame.Rect(x, y_lower, tubes.tube_width, dy_lower))
        pygame.draw.rect(screen, (0,255,60), pygame.Rect(x, y_upper, tubes.tube_width, dy_upper))

def checkCollision():
    pass
    

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")
    
    flapped = pygame.key.get_pressed()[pygame.K_SPACE]
    pygame.draw.circle(screen, (255,0,0), (bird.x, bird.y), bird.radius)
    bird.update(flapped)
    
    heights = tubes.updateTubePosition()
    renderTubes()

    pygame.display.flip() # update screen

    clock.tick(60)  # limits FPS to 60

pygame.quit()