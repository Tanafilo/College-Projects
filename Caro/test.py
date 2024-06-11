import pygame
import sys

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
FONT_SIZE = 80

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)

# Button Texts
one_min_text = font.render("1 minute", True, WHITE)
two_min_text = font.render("2 minutes", True, WHITE)

# Button Rectangles
one_min_button = one_min_text.get_rect(center=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100))
two_min_button = two_min_text.get_rect(center=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))

def timer_menu_display():
    while True:
        screen.fill((0, 0, 0))  # Fill screen with black background

        # Blit button texts
        screen.blit(one_min_text, one_min_button)
        screen.blit(two_min_text, two_min_button)

        pygame.display.flip()  # Update the display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Mouse Clicked at: {event.pos}")  # Debug print

                if one_min_button.collidepoint(event.pos):
                    print("1 minute button clicked")  # Debug print

                if two_min_button.collidepoint(event.pos):
                    print("2 minutes button clicked")  # Debug print

        clock.tick(60)

# Call the timer menu display function
timer_menu_display()
