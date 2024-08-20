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

current_tube_index = 0

def renderTubes(heights):
    for i, height in enumerate(heights):
        x = tubes.x + i * tubes.tube_xgap
        y_lower = screen_dim[1] - height
        y_upper = 0
        dy_lower = height
        dy_upper = screen_dim[1] - height - tubes.tube_ygap
        pygame.draw.rect(screen, (0, 255, 60), pygame.Rect(x, y_lower, tubes.tube_width, dy_lower))
        pygame.draw.rect(screen, (0, 255, 60), pygame.Rect(x, y_upper, tubes.tube_width, dy_upper))

def updateCurrentTube():
    global current_tube_index
    current_tube_right = tubes.x + tubes.tube_width + current_tube_index * tubes.tube_xgap
    # if the bird completely passes the current tube
    if current_tube_right < bird.x - bird.radius:
        current_tube_index += 1
        print('\n')

def checkCollision():
    global current_tube_index

    bird_right_edge = bird.x + bird.radius
    bird_left_edge = bird.x - bird.radius
    bird_top_edge = bird.y - bird.radius
    bird_bottom_edge = bird.y + bird.radius

    # Calculate the current tube's x position
    current_tube_x = tubes.x + current_tube_index * tubes.tube_xgap
    
    # Get the current tube's bottom and top height  
    tube_lower_y = screen_dim[1] - tubes.tube_heights[current_tube_index]
    tube_upper_y = tube_lower_y - tubes.tube_ygap
    
    # Check if the bird is horizontally within the tube's x bounds
    if bird_right_edge > current_tube_x and bird_left_edge < current_tube_x + tubes.tube_width:
        # Check collision with the bottom tube
        if bird_bottom_edge > tube_lower_y:
            return True
        # Check collision with the top tube
        elif bird_top_edge < tube_upper_y:
            return True
    
    return False



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")
    
    flapped = pygame.key.get_pressed()[pygame.K_SPACE]
    pygame.draw.circle(screen, (255, 0, 0), (bird.x, bird.y), bird.radius)
    heights = tubes.updateTubePosition()
    
    bird.update(flapped)
    collided = checkCollision()
    renderTubes(heights)
    if collided:
        print('OH NO!!!')

    updateCurrentTube()
    pygame.display.flip()  # update screen

    clock.tick(60)  # limits FPS to 60

pygame.quit()


