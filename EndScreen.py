import pygame

def show_end_screen(screen, screen_dim, score):
    font = pygame.font.SysFont(None, 75)
    small_font = pygame.font.SysFont(None, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill("black")

        # Display "Game Over" message
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(screen_dim[0] // 2, screen_dim[1] // 3))
        screen.blit(game_over_text, game_over_rect)

        # Display score
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(screen_dim[0] // 2, screen_dim[1] // 2))
        screen.blit(score_text, score_rect)

        # Display restart instruction
        restart_text = small_font.render("Press SPACE to Restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(screen_dim[0] // 2, screen_dim[1] // 2 + 80))
        screen.blit(restart_text, restart_rect)

        # Display exit instruction
        exit_text = small_font.render("Press ESC to Exit", True, (255, 255, 255))
        exit_rect = exit_text.get_rect(center=(screen_dim[0] // 2, screen_dim[1] // 2 + 140))
        screen.blit(exit_text, exit_rect)

        # Check for key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:  # Restart the game
            return
        if keys[pygame.K_ESCAPE]:  # Exit the game
            pygame.quit()
            exit()

        pygame.display.flip()
