import pygame
from Tubes import Tubes
from Bird import Bird
from EndScreen import show_end_screen

def main_game():
    pygame.init()
    screen_dim = (600, 720)
    screen = pygame.display.set_mode(screen_dim)
    clock = pygame.time.Clock()

    # Load the background image
    background_image = pygame.image.load("background.png").convert()
    background_image = pygame.transform.scale(background_image, screen_dim)  # Scale to fit the screen

    tubes = Tubes(screen_dim)
    bird = Bird(screen_dim)

    current_tube_index = 0
    score = 0
    font = pygame.font.SysFont(None, 55)

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
        nonlocal current_tube_index, score
        current_tube_right = tubes.x + tubes.tube_width + current_tube_index * tubes.tube_xgap
        # If the bird completely passes the current tube
        if current_tube_right < bird.x - bird.radius:
            current_tube_index += 1
            score += 1

    def renderScore():
        score_text = font.render(f'{score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))  # Display the score at the top left corner of the screen

    def checkCollision():
        nonlocal current_tube_index

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

        # Check if the bird is touching the top or bottom of the screen
        if bird_bottom_edge >= screen_dim[1] or bird_top_edge <= 0:
            return True

        return False

    # Main game loop
    running = True
    game_started = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with the background image
        screen.blit(background_image, (0, 0))

        # Render the bird and tubes in their initial positions
        bird.render(screen)
        renderTubes(tubes.tube_heights)
        renderScore()

        # Check if space bar is pressed to start the game
        keys = pygame.key.get_pressed()
        if not game_started and keys[pygame.K_SPACE]:
            game_started = True

        # If the game has started, update bird and tubes
        if game_started:
            flapped = keys[pygame.K_SPACE]
            bird.update(flapped)
            heights = tubes.updateTubePosition()

            collided = checkCollision()
            renderTubes(heights)

            if collided:
                show_end_screen(screen, screen_dim, score)  # Show the end screen when the game ends
                return  # Restart the game by returning from the main_game function

            updateCurrentTube()

        pygame.display.flip()  # Update screen

        clock.tick(60)  # Limit FPS to 60

    pygame.quit()

if __name__ == "__main__":
    while True:
        main_game()  # Restart the game each time it ends
