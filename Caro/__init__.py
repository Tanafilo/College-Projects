from config import *


class UI:
    def __init__(self):
        pass         


    def __draw_splash_screen(self):
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
        # Draw loading bar
        pygame.draw.rect(screen, loading_bar_color, (SCREEN_WIDTH // 4, (SCREEN_HEIGHT) // 2 + 50, (SCREEN_WIDTH // 2) * progress, 20), 0)

        # Draw loading percentage
        percentage_text = splash_font.render(f"{int(progress * 100)}%", True, WHITE)
        
        screen.blit(percentage_text, ((SCREEN_WIDTH - percentage_text.get_width()) // 2, (SCREEN_HEIGHT) // 2 + 80))
        
        
    def splash_screen(self, duration):
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
        menu = pygame.image.load("Images/menu.png")

        menu = pygame.transform.scale(menu, (SCREEN_WIDTH, SCREEN_HEIGHT))

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
        while True:
            start_button, time_button, exit_button = self.__draw_main_menu()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos): # Press start
                        return  # Start the game
                    
                    elif time_button.collidepoint(event.pos): # Press time
                        print("Time Set button clicked")  # Placeholder for setting time functionality

                    elif exit_button.collidepoint(event.pos): # Press exit
                        self.terminate()

            clock.tick(60)


    def end_screen():
        pass


    def terminate(self):
        pygame.quit()

        exit()

class Setting():
    def __init__(self):
        pass


    def name_display(self):
        name_font = pygame.font.Font(None, 70)

        name_1 = name_font.render("Player 1", True, WHITE)
        
        name_2 = name_font.render("PLayer 2", True, WHITE)

        screen.blit(name_1, (80, SCREEN_HEIGHT * 1 // 8 - 105))

        screen.blit(name_2, (80, SCREEN_HEIGHT - 60))
        
        screen.blit(avatar_1, (100 + BOARD_WIDTH, SCREEN_HEIGHT * 1 // 8 - 100))

        screen.blit(avatar_2, (100 + BOARD_WIDTH, SCREEN_HEIGHT * 7 // 8 - 55))

    def time_display():
        pass


    def scoreboard_display():
        pass


    def stalemate():
        pass


    def forfeit():
        pass


    def option_display():
        pass
    

class Game(UI, Setting):
    def __init__(self, player = 1):
        self.board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        
        self.player = player

        self.space = 80


    def draw_board(self):
        screen.blit(background, (0, 0))

        # Draw grid
        for width in range(BOARD_SIZE + 1):
            pygame.draw.line(screen, WHITE, 
                             (width * CELL_SIZE + self.space, self.space), (width * CELL_SIZE + self.space, BOARD_WIDTH + self.space), BORDER_WIDTH)

        for height in range(BOARD_SIZE + 1):
            pygame.draw.line(screen, WHITE, 
                             (self.space, height * CELL_SIZE + self.space), (BOARD_WIDTH + self.space, height * CELL_SIZE + self.space), BORDER_WIDTH)

        self.name_display()


    def draw_piece(self, column, row):
        self.board[row][column] = self.player

        if self.player == 1:
            screen.blit(player1, (column * CELL_SIZE + self.space, row * CELL_SIZE + self.space))
        else:
            screen.blit(player2, (column * CELL_SIZE + self.space, row * CELL_SIZE + self.space))

        self.player = 3 - self.player


    def start():
        pass


    def check_winner():
        pass


    def end():
        pass

