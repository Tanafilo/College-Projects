from config import *

class UI:
    """
    User Interface class responsible for rendering various screens
    such as splash screen, main menu, and end screen.
    """
    def __init__(self):
        self.__time = 10 * 60


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

        # Exit
        exit_text = button_font.render("Exit", True, WHITE)
        exit_button = exit_text.get_rect(center=(SCREEN_WIDTH * 7 // 8 - 20, SCREEN_HEIGHT * 3 // 4 + 80))
        screen.blit(exit_text, exit_button)

        # Update
        pygame.display.flip()

        return start_button, exit_button


    def main_menu(self):
        """
        Displays the main menu and handles interactions.
        """
        while True:
            start_button, exit_button = self.__draw_main_menu()
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):  # Press start
                        self.timer_menu()

                        return

                    elif exit_button.collidepoint(event.pos):  # Press exit
                        self.terminate()

            
            clock.tick(60)


    def __timer_menu_display(self):
        """
        Draws timer menu with 6 timer options
        """
        font = pygame.font.Font(None, 80)

        screen.blit(timer_menu, (0, 0))
        
        set_time = font.render("Set time", True, loading_bar_color)
        screen.blit(set_time, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 200))

        # 1, 2, 5, 10, 15, 30 minutes
        one_min = font.render("1 minute", True, loading_bar_color)
        one_min_button = one_min.get_rect(center=(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 70))
        
        two_min = font.render("2 minute", True, loading_bar_color)
        two_min_button = two_min.get_rect(center=(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 30))
        
        five_min = font.render("5 minute", True, loading_bar_color)
        five_min_button = five_min.get_rect(center=(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 130))
                
        ten_min = font.render("10 minute", True, loading_bar_color)
        ten_min_button = ten_min.get_rect(center=(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT // 2 - 70))

        fifteen_min = font.render("15 minute", True, loading_bar_color)
        fifteen_min_button = fifteen_min.get_rect(center=(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT // 2 + 30))

        thirty_min = font.render("30 minute", True, loading_bar_color)
        thirty_min_button = thirty_min.get_rect(center=(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT // 2 + 130))

        screen.blit(one_min, one_min_button)
        
        screen.blit(two_min, two_min_button)
        
        screen.blit(five_min, five_min_button)
        
        screen.blit(ten_min, ten_min_button) 
        
        screen.blit(fifteen_min, fifteen_min_button)
        
        screen.blit(thirty_min, thirty_min_button)

        pygame.display.flip()

        return one_min_button, two_min_button, five_min_button, ten_min_button, fifteen_min_button, thirty_min_button


    def timer_menu(self):
        """
        Displays the timer menu and handle interactions
        """
        while True:
            one_min_button, two_min_button, five_min_button, ten_min_button, fifteen_min_button, thirty_min_button = self.__timer_menu_display()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if one_min_button.collidepoint(event.pos):  
                        self.__time = 1 * 60

                        return
                    
                    elif two_min_button.collidepoint(event.pos):  
                        self.__time = 2 * 60

                        return
                
                    elif five_min_button.collidepoint(event.pos):  
                        self.__time = 5 * 60

                        return

                    elif ten_min_button.collidepoint(event.pos):  
                        self.__time = 10 * 60

                        return
                    
                    elif fifteen_min_button.collidepoint(event.pos):  
                        self.__time = 15 * 60

                        return

                    elif thirty_min_button.collidepoint(event.pos):  
                        self.__time = 30 * 60

                        return

            clock.tick(60)

            
    def get_time(self):
        return self.__time


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

        if winner != 0: # No draw
            winner = font.render(f"Player {winner} Won", True, PINK_RED)
        
        else: # Draw
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
                    self.terminate()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.collidepoint(event.pos):
                        return
                    

    def terminate(self):
        """
        Terminates the Pygame instance and exits the program.
        """
        pygame.quit()

        exit()


class Time:
    def __init__(self, match_time):
        self.player1_time = match_time
        
        self.player2_time = match_time 
        
        self.last_update_time = time.time()

    def update_check(self, current_player, pause):
        """
        Updates the time and check for any winning player by timeout

        Args:
            current_player (int): shows the current player
        """
        if pause:
            return None

        current_time = time.time()
        
        elapsed_time = current_time - self.last_update_time
        
        self.last_update_time = current_time

        if current_player == 1:
            self.player1_time -= elapsed_time

            if self.player1_time <= 0:
                return 2  # Player 2 wins by timeout
        else:
            self.player2_time -= elapsed_time

            if self.player2_time <= 0:
                return 1  # Player 1 wins by timeout

        return None  # No winner by timeout


    def display(self):
        """
        Draw the timer box in the game
        """
        pygame.draw.rect(screen, loading_bar_color, pygame.Rect(SCREEN_WIDTH // 2 - 118, 10, 200, 60))

        pygame.draw.rect(screen, loading_bar_color, pygame.Rect(SCREEN_WIDTH // 2 - 118, SCREEN_HEIGHT - 68, 200, 60))
        
        # Player 1 timer
        timer_font = pygame.font.Font(None, 70)

        player1_minutes = int(self.player1_time) // 60

        player1_seconds = int(self.player1_time) % 60

        player1_time_text = f"{player1_minutes:02}:{player1_seconds:02}"
        
        player1_timer = timer_font.render(f"{player1_time_text}", True, WHITE)
        
        screen.blit(player1_timer, (SCREEN_WIDTH // 2 - 80, 17))

        # Player 2 timer
        player2_minutes = int(self.player2_time) // 60
        
        player2_seconds = int(self.player2_time) % 60
        
        player2_time_text = f"{player2_minutes:02}:{player2_seconds:02}"
        
        player2_timer = timer_font.render(f"{player2_time_text}", True, WHITE)
        
        screen.blit(player2_timer, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT - 60))
        

        pygame.display.flip()


class Setting:
    """
    Settings class for managing and displaying various game settings
    such as player names, time, and scores.
    """  
    def __draw(self):
        """
        Displays draw option
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


    def option_display(self, score):
        """
        Displays game options.
        """
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
        super().__init__()

        self.__player = player
        
        self.__score = [0] * 2

        self.__paused = False

        
    def __board_display(self):
        """
        Draws the game board with grid lines.
        """
        self.__board_space = 80

        screen.blit(background, (0, 0))

        # Draw grid
        for width in range(BOARD_SIZE + 1):
            pygame.draw.line(screen, WHITE, 
                             (width * CELL_SIZE + self.__board_space, self.__board_space), 
                             (width * CELL_SIZE + self.__board_space, BOARD_WIDTH + self.__board_space), BORDER_WIDTH)

        for height in range(BOARD_SIZE + 1):
            pygame.draw.line(screen, WHITE, 
                             (self.__board_space, height * CELL_SIZE + self.__board_space), 
                             (BOARD_WIDTH + self.__board_space, height * CELL_SIZE + self.__board_space), BORDER_WIDTH)


    def __piece_display(self, column, row):
        """
        Draws a piece on the board at the specified column and row.
        
        Args:
            column (int): The column index for the piece.
            row (int): The row index for the piece.
        """
        self.__board[row][column] = self.__player

        if self.__board[row][column] == 1:
            screen.blit(player1, (column * CELL_SIZE + self.__board_space, row * CELL_SIZE + self.__board_space))

        elif self.__board[row][column] == 2:
            screen.blit(player2, (column * CELL_SIZE + self.__board_space, row * CELL_SIZE + self.__board_space))

        self.__player = 3 - self.__player
    

    def __player_display(self):
        """
        Displays the names and avatars of the players.
        """
        name_font = pygame.font.Font(None, 70)
        name_1 = name_font.render("Player 1", True, WHITE)
        name_2 = name_font.render("Player 2", True, WHITE)

        screen.blit(name_1, (80, SCREEN_HEIGHT * 1 // 8 - 105))
        screen.blit(name_2, (80, SCREEN_HEIGHT - 60))
        screen.blit(avatar_1, (100 + BOARD_WIDTH, SCREEN_HEIGHT * 1 // 8 - 100))
        screen.blit(avatar_2, (100 + BOARD_WIDTH, SCREEN_HEIGHT * 7 // 8 - 55))


    def __scoreboard_display(self):
        """
        Displays the scoreboard.
        """
        font = pygame.font.Font(None, 120)

        score_board = font.render(f"{self.__score[0]} : {self.__score[1]}", True, loading_bar_color)

        screen.blit(score_board, (SCREEN_WIDTH * 7/8 - score_board.get_width(), SCREEN_HEIGHT * 2/8))

    
    def pause_game(self):
        """
        Displays Pause game screen and handles interactions
        """
        self.__paused = True
        
        screen.blit(pause_game, (0, 0))

        font = pygame.font.Font(None, 100)
        
        pause_text = font.render("Game Paused", True, WHITE)
        
        screen.blit(pause_text, ((SCREEN_WIDTH - pause_text.get_width()) // 2, SCREEN_HEIGHT // 2 - 75))

        font = pygame.font.Font(None, 85)

        resume_text = font.render("Press any key to resume", True, WHITE)

        screen.blit(resume_text, ((SCREEN_WIDTH - resume_text.get_width()) // 2, SCREEN_HEIGHT // 2 + 50))
        
        pygame.display.flip()

        while self.__paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()

                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    self.__paused = False
                    
                    self.__timer.last_update_time = time.time()  # Update timer to avoid jump
    

    def __redraw_pieces(self):
        """
        Redraw all pieces on the board based on the current board state.
        """
        for row in range(BOARD_SIZE):
            for column in range(BOARD_SIZE):
                if self.__board[row][column] == 1:
                    screen.blit(player1, (column * CELL_SIZE + self.__board_space, row * CELL_SIZE + self.__board_space))

                elif self.__board[row][column] == 2:
                    screen.blit(player2, (column * CELL_SIZE + self.__board_space, row * CELL_SIZE + self.__board_space))

    

    def start_game(self):
        """
        Initializes the game board, draws the board, adds UI, and run the game
        """
        self.__board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)] # Reset board
        
        self.__timer = Time(self.get_time())
        
        first_player = self.__player

        # Displays all the basics 
        self.__board_display()
        
        self.__player_display()

        self.__scoreboard_display()

        # Game buttons
        draw_button, resign_button, pause_button, menu_button, exit_button = self.option_display(self.__score)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__paused:
                        continue

                    width, height = event.pos

                    column = (width - self.__board_space) // CELL_SIZE
                    row = (height - self.__board_space) // CELL_SIZE

                    if 0 <= column < BOARD_SIZE and 0 <= row < BOARD_SIZE and self.__board[row][column] == 0:
                        self.__piece_display(column, row)

                    if draw_button.collidepoint(event.pos): # Draw
                        self.__player = 3 - first_player

                        self.__check_endgame(0)

                    elif resign_button.collidepoint(event.pos): # Resign
                        self.__check_endgame(3 - self.__player)

                    elif pause_button.collidepoint(event.pos): # Pause
                        self.pause_game()

                        # Displays all the basics 
                        self.__board_display()
                        
                        self.__player_display()

                        self.__scoreboard_display()

                        # Game buttons
                        draw_button, resign_button, pause_button, menu_button, exit_button = self.option_display(self.__score)
                        
                        self.__redraw_pieces()

                    elif menu_button.collidepoint(event.pos): # Back to main menu
                        self.main_menu()

                        self.splash_screen(3.5)

                        self.start_game()

                    elif exit_button.collidepoint(event.pos): # Exit game
                        self.terminate()
                    
                    self.__check_endgame(self.__check_winner())
            
            self.__timer.display()
            
            self.__check_endgame(self.__timer.update_check(self.__player, self.__paused))

            pygame.display.flip()


    def __check_winner(self):
        """
        Checks horizontal, vertical, and diagonal for a winner
        """
        for row in range(BOARD_SIZE):
            for column in range(BOARD_SIZE):
                # Check horizontal
                if column < BOARD_SIZE - 4 and all(self.__board[row][column] == self.__board[row][column + i] != 0 for i in range(5)):
                    return self.__board[row][column]
                
                # Check vertical
                if row < BOARD_SIZE - 4 and all(self.__board[row][column] == self.__board[row + i][column] != 0 for i in range(5)):
                    return self.__board[row][column] 
               
                # Check diagonal (down-right)
                if row < BOARD_SIZE - 4 and column < BOARD_SIZE - 4 and all(self.__board[row][column] == self.__board[row + i][column + i] != 0 for i in range(5)):
                    return self.__board[row][column]

                # Check diagonal (down-left)
                if row >= 4 and column < BOARD_SIZE - 4 and all(self.__board[row][column] == self.__board[row - i][column + i] != 0 for i in range(5)):
                    return self.__board[row][column]

        return None

    
    def __check_endgame(self, winner):
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
                self.__player = 1

            elif self.__score[0] > self.__score[1]:
                self.__player = 2
            
            self.game_over_screen(winner)
            
            self.start_game()


#help(UI)
#help(Setting)
#help(Game)
