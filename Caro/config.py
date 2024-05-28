# Configurations

import pygame

import time

pygame.init()

# Constants
BOARD_SIZE = 24 # 24x24 Board
CELL_SIZE = 35
BOARD_WIDTH = BOARD_SIZE * CELL_SIZE
SCREEN_WIDTH = BOARD_SIZE * CELL_SIZE + 600
SCREEN_HEIGHT = BOARD_SIZE * CELL_SIZE + 160
BORDER_WIDTH = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
loading_bar_color = (255, 183, 77)
loading_bar_bg_color = (220, 220, 220)

# Set up
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Caro Game")

app_icon = pygame.image.load("Images/app_icon.png")
pygame.display.set_icon(app_icon)

# Load images
background = pygame.image.load("Images/background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

player1 = pygame.image.load("Images/icon1.png")
player1 = pygame.transform.scale(player1, (CELL_SIZE, CELL_SIZE))

player2 = pygame.image.load("Images/icon2.png")
player2 = pygame.transform.scale(player2, (CELL_SIZE, CELL_SIZE))

splash_icon = pygame.transform.scale(app_icon, (100, 100))
splash_font = pygame.font.Font(None, 50)

avatar_1 = pygame.image.load("Images/avatar1.png")
avatar_1 = pygame.transform.scale(avatar_1, (160, 160))

avatar_2 = pygame.image.load("Images/avatar2.png")
avatar_2 = pygame.transform.scale(avatar_2, (160, 160))

# FPS
clock = pygame.time.Clock()
