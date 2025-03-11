import pygame
from static_variables import *
from Buttons.FancyButtons import FancyButton
from Buttons.RadioButton import RadioButton
class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.start_game = False
        self.settings_game = False
        self.back_game = False
        self.button_width = 300
        self.button_height = 90
        self.spacing = 40
        self.fullscreen = True
        self.total_width = (3 * self.button_width) + (2 * self.spacing)
        self.start_x = (WIDTH - self.total_width) // 2
        self.start_y = HEIGHT // 2

        # Make the buttons 20% smaller
        small_button_width = int(self.button_width * 0.8)
        small_button_height = int(self.button_height * 0.8)

        # Calculate the total width for the first row (Resume + Settings buttons + spacing between them)
        first_row_width = small_button_width * 2 + self.spacing

        # Calculate the starting X position to center the buttons (taking the combined width into account)
        first_row_x = WIDTH // 2 - first_row_width // 2  # Centering the first row of buttons

        # Create new buttons with smaller dimensions and properly centered
        self.resume_button = FancyButton("Resume", first_row_x, HEIGHT // 2 - 50, small_button_width, small_button_height,
                                    BUTTON_COLOR, BUTTON_HOVER)
        self.settings_button = FancyButton("Settings", first_row_x + small_button_width + self.spacing, HEIGHT // 2 - 50,
                                      small_button_width, small_button_height, BUTTON_COLOR, BUTTON_HOVER)

        # Quit button width is as wide as Resume + Settings buttons combined, centered below the first row
        self.quit_button = FancyButton("Quit", WIDTH // 2 - (small_button_width * 2 + self.spacing) // 2, HEIGHT // 2 + 100,
                                  small_button_width * 2 + self.spacing, small_button_height, BUTTON_COLOR, BUTTON_HOVER)

    # Pause menu background
    pygame.draw.rect(screen, (50, 50, 50), (WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2), border_radius=20)
    def draw_menu(self):
        # Draw buttons
        self.resume_button.draw(screen)
        self.settings_button.draw(screen)
        self.quit_button.draw(screen)

    def handle_event(self, event):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_paused = False
                self.in_main_menu = True  # Transition to main menu when quitting
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.resume_button.is_clicked():
                    self.game_paused = False  # Resume the game
                if self.settings_button.is_clicked():
                    settings_menu()  # Go to settings menu
                if quit_button.is_clicked():
                    game_paused = False
                    main_menu()  # Go to main menu