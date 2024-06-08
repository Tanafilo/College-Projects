from config import *

class UI:
    """
    User Interface class responsible for rendering various screens
    such as splash screen, main menu, and end screen.
    """
    def __draw_splash_screen(self):
        """
        Draws the splash screen with the loading icon, game name, and loading bar background.
        """
        screen.blit(background, (0, 0))

        # Draw icon
        screen.blit(splash_icon, ((SCREEN_WIDTH - 100) // 2, (SCREEN_HEIGHT - 100) // 2 - 60))

        # Draw text
        text_surface = splash_font.render("Caro Game", True, WHITE)
        screen.blit(text_surface, ((SCREEN_WIDTH - text_surface.get_width()) // 2, (SCREEN_HEIGHT) // 2))

        # Draw loading bar background
        pygame.draw.rect(screen, loading_bar_bg_color,
                         (SCREEN_WIDTH // 4, (SCREEN_HEIGHT) // 2 + 50, SCREEN_WIDTH // 2, 20), 0)


    def __update_loading_bar(self, progress):
        """
        Updates the loading bar based on the current progress.
        
        Args:
            progress (float): The current progress as a fraction between 0 and 1.
        """
        # Draw loading bar
        pygame.draw.rect(screen, loading_bar_color, 
                         (SCREEN_WIDTH // 4, (SCREEN_HEIGHT) // 2 + 50, (SCREEN_WIDTH // 2) * progress, 20), 0)

        # Draw loading percentage
        percentage_text = splash_font.render(f"{int(progress * 100)}%", True, WHITE)
        screen.blit(percentage_text, ((SCREEN_WIDTH - percentage_text.get_width()) // 2, (SCREEN_HEIGHT) // 2 + 80))


    def splash_screen(self, duration):
        """
        Displays the splash screen for a given duration.
        
        Args:
            duration (int): Duration in seconds for which the splash screen should be displayed.
        """
        start_time = time.time()

        while time.time() - start_time < duration:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()

            self.__draw_splash_screen()
            
            elapsed_time = time.time() - start_time
            progress = elapsed_time / duration
            
            self.__update_loading_bar(progress)
            pygame.display.flip()
            clock.tick(60)


    def __draw_main_menu(self):
        """
        Draws the main menu screen with buttons for starting the game, setting the time, and exiting the game.
        """
        screen.blit(menu, (0, 0))

        # Draw icon and game name
        title_font = pygame.font.Font(None, 100)
        screen.blit(splash_icon, (80, 50))
        game_title = title_font.render("Caro Game", True, WHITE)
        screen.blit(game_title, (200, 65))

        # Draw buttons
        button_font = pygame.font.Font(None, 70)

        # Start
        start_text = button_font.render("Start Game", True, WHITE)
        start_button = start_text.get_rect(center=(SCREEN_WIDTH * 7 // 8 - 20, SCREEN_HEIGHT * 3 // 4 - 10))
        screen.blit(start_text, start_button)

        # Time
        time_text = button_font.render("Time Set", True, WHITE)
        time_button = time_text.get_rect(center=(SCREEN_WIDTH * 7 // 8 - 20, SCREEN_HEIGHT * 3 // 4 + 80))
        screen.blit(time_text, time_button)

        # Exit
        exit_text = button_font.render("Exit", True, WHITE)
        exit_button = exit_text.get_rect(center=(SCREEN_WIDTH * 7 // 8 - 20, SCREEN_HEIGHT * 3 // 4 + 170))
        screen.blit(exit_text, exit_button)

        # Update
        pygame.display.flip()
        return start_button, time_button, exit_button


    def main_menu(self):
        """
        Displays the main menu screen and handles button interactions.
        """
        while True:
            start_button, time_button, exit_button = self.__draw_main_menu()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):  # Press start
                        return
                    
                    elif time_button.collidepoint(event.pos):  # Press time
                        print("Time Set button clicked")  # Placeholder for setting time functionality

                    elif exit_button.collidepoint(event.pos):  # Press exit
                        self.terminate()

            clock.tick(60)


    def game_over_screen(self, winner):
        """
        Displays the game over screen.

        Args:
            winner (int): winning player
        """
        screen.blit(game_over_bg, (0, 0))

        # Game over text
        font = pygame.font.Font(None, 150)
        game_over = font.render("Game Over", True, PINK_RED)
        screen.blit(game_over, ((SCREEN_WIDTH - game_over.get_width()) // 2, SCREEN_HEIGHT // 2 - 250))
                
        # Winner text
        font = pygame.font.Font(None, 80)
        if winner != 0:
            winner = font.render(f"Player {winner} Won", True, PINK_RED)
        
        else:
            winner = font.render("Match Draw", True, PINK_RED)

        screen.blit(winner, ((SCREEN_WIDTH - winner.get_width()) // 2, SCREEN_HEIGHT // 2 - 80))

        # Restart button
        font = pygame.font.Font(None, 80)
        restart_text = font.render("Restart Now", True, WHITE)
        restart_button = restart_text.get_rect(center=((SCREEN_WIDTH) // 2, SCREEN_HEIGHT // 2 + 80))
        screen.blit(restart_text, restart_button)

        pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Caro.terminate()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.collidepoint(event.pos):
                        return


    def terminate(self):
        """
        Terminates the Pygame instance and exits the program.
        """
        pygame.quit()

        exit()


class Setting:
    """
    Settings class for managing and displaying various game settings
    such as player names, time, and scores.
    """  
    def __name_display(self):
        """
        Displays the names of the players.
        """
        name_font = pygame.font.Font(None, 70)
        name_1 = name_font.render("Player 1", True, WHITE)
        name_2 = name_font.render("Player 2", True, WHITE)

        screen.blit(name_1, (80, SCREEN_HEIGHT * 1 // 8 - 105))
        screen.blit(name_2, (80, SCREEN_HEIGHT - 60))
        screen.blit(avatar_1, (100 + BOARD_WIDTH, SCREEN_HEIGHT * 1 // 8 - 100))
        screen.blit(avatar_2, (100 + BOARD_WIDTH, SCREEN_HEIGHT * 7 // 8 - 55))


    def __time_display(self):
        """
        Displays the time settings (placeholder).
        """
        pass


    def __scoreboard_display(self, score):
        """
        Displays the scoreboard.

        Args:
            score (list): Store the player score
        """
        font = pygame.font.Font(None, 120)

        score_board = font.render(f"{score[0]} : {score[1]}", True, loading_bar_color)

        screen.blit(score_board, (SCREEN_WIDTH * 7/8 - score_board.get_width(), SCREEN_HEIGHT * 2/8))


    def __draw(self):
        """
        Displays stalemate option
        """
        font = pygame.font.Font(None, 65)

        draw_text = font.render("Draw", True, WHITE)

        draw_button = draw_text.get_rect(center=(SCREEN_WIDTH * 6/8 - draw_text.get_width() + 60, SCREEN_HEIGHT * 2/5))
        
        screen.blit(draw_text, draw_button)

        return draw_button


    def __resign(self):
        """
        Displays resign option 
        """
        font = pygame.font.Font(None, 65)

        resign_text = font.render("Resign", True, WHITE)

        resign_button = resign_text.get_rect(center=(SCREEN_WIDTH - resign_text.get_width() + 20, SCREEN_HEIGHT * 2/5))
        
        screen.blit(resign_text, resign_button)

        return resign_button


    def __exit(self):
        """
        Displays exit option.
        """
        font = pygame.font.Font(None, 60)

        exit_text = font.render("EXIT GAME", True, PINK_RED)

        exit_button = exit_text.get_rect(center=(SCREEN_WIDTH - exit_text.get_width() + 70, SCREEN_HEIGHT - 50))
        
        screen.blit(exit_text, exit_button)
        
        return exit_button


    def __pause(self):
        """
        Displays pause button
        """
        font = pygame.font.Font(None, 65)

        pause_text = font.render("Pause Game", True, PURPLE)

        pause_button = pause_text.get_rect(center=(SCREEN_WIDTH - pause_text.get_width() + 10, SCREEN_HEIGHT * 3/5 - 80))
        
        screen.blit(pause_text, pause_button)

        return pause_button


    def __to_main_menu(self):
        """
        Displays back-to-main-menu button
        """
        font = pygame.font.Font(None, 65)

        to_main_menu_text = font.render("Back To Main Menu", True, EMERALD)

        to_main_menu_button = to_main_menu_text.get_rect(center=(SCREEN_WIDTH - to_main_menu_text.get_width() + 155, SCREEN_HEIGHT * 3/5 + 30))
        
        screen.blit(to_main_menu_text, to_main_menu_button)
        
        return to_main_menu_button


    def __agreement(self):
        """
        Displays confirmation box to make sure of the user choice
        
        Args:
            prompt (string): the prompt displayed in the text box
        """
        

    def option_display(self, score):
        """
        Displays game options.

        Args:
            score (list): store the player score
        """
        # Display buttons
        self.__name_display()
        
        self.__time_display()

        self.__scoreboard_display(score)

        return self.__draw(), self.__resign(), self.__pause(), self.__to_main_menu(), self.__exit()
                

class Game(UI, Setting):
    """
    Main Game class inheriting from UI and Setting classes, responsible for
    managing the game state, drawing the board, and handling player moves.
    """    
    def __init__(self, player = 1):
        """
        Sets the starting player.
        
        Args:
            player (int): The player (1 or 2).
            __score (int list): Store the score of each player
        """
        self.player = player
        
        self.space = 80

        self.__score = [0] * 2

    
    def draw_board(self):
        """
        Draws the game board with grid lines.
        """
        screen.blit(background, (0, 0))

        # Draw grid
        for width in range(BOARD_SIZE + 1):
            pygame.draw.line(screen, WHITE, 
                             (width * CELL_SIZE + self.space, self.space), 
                             (width * CELL_SIZE + self.space, BOARD_WIDTH + self.space), BORDER_WIDTH)

        for height in range(BOARD_SIZE + 1):
            pygame.draw.line(screen, WHITE, 
                             (self.space, height * CELL_SIZE + self.space), 
                             (BOARD_WIDTH + self.space, height * CELL_SIZE + self.space), BORDER_WIDTH)


    def draw_piece(self, column, row):
        """
        Draws a piece on the board at the specified column and row.
        
        Args:
            column (int): The column index for the piece.
            row (int): The row index for the piece.
        """
        self.board[row][column] = self.player

        if self.player == 1:
            screen.blit(player1, (column * CELL_SIZE + self.space, row * CELL_SIZE + self.space))
        else:
            screen.blit(player2, (column * CELL_SIZE + self.space, row * CELL_SIZE + self.space))

        self.player = 3 - self.player

    
    def start_game(self):
        """
        Initializes the game board, draws the board, adds UI, and run the game
        """
        self.board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)] # Reset board

        first_player = self.player
        
        self.draw_board()

        draw_button, resign_button, pause_button, menu_button, exit_button = self.option_display(self.__score)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    width, height = event.pos

                    column = (width - self.space) // CELL_SIZE
                    row = (height - self.space) // CELL_SIZE

                    if 0 <= column < BOARD_SIZE and 0 <= row < BOARD_SIZE and self.board[row][column] == 0:
                        self.draw_piece(column, row)

                    if draw_button.collidepoint(event.pos): # Draw
                        self.player = 3 - first_player

                        self.check_endgame(0)

                    elif resign_button.collidepoint(event.pos): # Resign
                        self.check_endgame(3 - self.player)

                    elif pause_button.collidepoint(event.pos): # Pause
                        return

                    elif menu_button.collidepoint(event.pos): # Back to main menu
                        self.main_menu()

                        self.splash_screen(0)

                        self.start_game()

                    elif exit_button.collidepoint(event.pos): # Exit game
                        self.terminate()
                    
                    self.check_endgame(self.__check_winner())

            pygame.display.flip()

    def __check_winner(self):
        """
        Checks horizontal, vertical, and diagonal for a winner
        """
        for row in range(BOARD_SIZE):
            for column in range(BOARD_SIZE):
                # Check horizontal
                if column < BOARD_SIZE - 4 and all(self.board[row][column] == self.board[row][column + i] != 0 for i in range(5)):
                    return self.board[row][column]
                
                # Check vertical
                if row < BOARD_SIZE - 4 and all(self.board[row][column] == self.board[row + i][column] != 0 for i in range(5)):
                    return self.board[row][column] 
               
                # Check diagonal (down-right)
                if row < BOARD_SIZE - 4 and column < BOARD_SIZE - 4 and all(self.board[row][column] == self.board[row + i][column + i] != 0 for i in range(5)):
                    return self.board[row][column]

                # Check diagonal (down-left)
                if row >= 4 and column < BOARD_SIZE - 4 and all(self.board[row][column] == self.board[row - i][column + i] != 0 for i in range(5)):
                    return self.board[row][column]

        return None

    
    def check_endgame(self, winner):
        """
        Checks for any winning player or match draw to load end game screen and reset the game

        Args:
            winner (int or None): winning player
        """
        if winner == 0:
            self.game_over_screen(0)

            self.start_game()

        elif winner is not None:
            self.__score[winner - 1] += 1

            if self.__score[0] < self.__score[1]: 
                self.player = 1

            elif self.__score[0] > self.__score[1]:
                self.player = 2
            
            self.game_over_screen(winner)
            
            self.start_game()


#help(UI)
#help(Setting)
#help(Game)
