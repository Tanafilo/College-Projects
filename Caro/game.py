# Game Programme

#from __init__ import *
#
#from config import *

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
BOARD_SIZE = 24 # 24x24 Board
CELL_SIZE = 30
SCREEN_SIZE = BOARD_SIZE * CELL_SIZE
WHITE = (255, 255, 255)
BORDER_WIDTH = 1

# Set up
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

pygame.display.set_caption("Caro Game")

icon = pygame.image.load("Images/app_icon.png")
pygame.display.set_icon(icon)

# Load images
background = pygame.image.load("Images/background.png")
background = pygame.transform.scale(background, (SCREEN_SIZE, SCREEN_SIZE))

player1 = pygame.image.load("Images/letter-x.png")
player1 = pygame.transform.scale(player1, (CELL_SIZE, CELL_SIZE))


player2 = pygame.image.load("Images/letter-o.png")
player2 = pygame.transform.scale(player2, (CELL_SIZE, CELL_SIZE))

# Game variables
board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
current_player = 1

def draw_board():
    # Draw background
    screen.blit(background, (0, 0))

    # Draw grid
    for x in range(0, SCREEN_SIZE, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_SIZE), BORDER_WIDTH)

    for y in range(0, SCREEN_SIZE, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (SCREEN_SIZE, y), BORDER_WIDTH)

def draw_piece(x, y, player):
    if player == 1:
        screen.blit(player1, (x * CELL_SIZE, y * CELL_SIZE))
    else:
        screen.blit(player2, (x * CELL_SIZE , y * CELL_SIZE))

# Main game loop
draw_board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            grid_x = x // CELL_SIZE
            grid_y = y // CELL_SIZE

            if board[grid_y][grid_x] == 0:
                board[grid_y][grid_x] = current_player

                draw_piece(grid_x, grid_y, current_player)

                current_player = 3 - current_player  # Switch player

    pygame.display.flip()

