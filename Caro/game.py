# Game Program

from config import *

from __init__ import *

# Main
Caro = Game()

Settings = Setting()

Caro.main_menu()

Caro.splash_screen(4)

Caro.draw_board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Caro.terminate()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            width, height = event.pos

            column = (width - Caro.space) // CELL_SIZE
            row = (height - Caro.space) // CELL_SIZE

            if 0 <= column < BOARD_SIZE and 0 <= row < BOARD_SIZE and Caro.board[row][column] == 0:
                Caro.draw_piece(column, row)

    pygame.display.flip()

