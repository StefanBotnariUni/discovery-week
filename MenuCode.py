from static_variables import *
from Buttons.FancyButtons import FancyButton
from Buttons.RadioButton import RadioButton
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.start_game = False
        self.settings_game = False
        self.pause_game = False
        self.back_game = False
        self.button_width = 300
        self.button_height = 90
        self.spacing = 40
        self.fullscreen = True
        self.total_width = (3 * self.button_width) + (2 * self.spacing)
        self.start_x = (WIDTH - self.total_width) // 2
        self.start_y = HEIGHT // 2
        self.small_button_width = int(self.button_width * 0.8)
        self.small_button_height = int(self.button_height * 0.8)
        self.first_row_width = self.small_button_width * 2 + self.spacing
        # Calculate the starting X position to center the buttons (taking the combined width into account)
        self.first_row_x = WIDTH // 2 - self.first_row_width // 2
        #Create buttons
        self.start_button = FancyButton("Start", self.start_x, self.start_y, self.button_width, self.button_height, BUTTON_COLOR, BUTTON_HOVER)
        self.settings_button = FancyButton("Settings", self.start_x + self.button_width + self.spacing, self.start_y, self.button_width,
                                      self.button_height,
                                      BUTTON_COLOR, BUTTON_HOVER)
        self.quit_button = FancyButton("Quit", self.start_x + (2 * self.button_width) + (2 * self.spacing), self.start_y, self.button_width,
                                  self.button_height,
                                  BUTTON_COLOR, BUTTON_HOVER)
        self.back_button = FancyButton(
            "Back",
            (WIDTH - self.button_width) // 2,  # Centered horizontally
            HEIGHT - self.button_height - 50,  # Slightly higher from the bottom
            self.button_width,
            self.button_height,
            BUTTON_COLOR,
            BUTTON_HOVER
        )
        self.small_resume_button = FancyButton("Resume", self.first_row_x, HEIGHT // 2 - 50, self.small_button_width,
                                         self.small_button_height,
                                         BUTTON_COLOR, BUTTON_HOVER)
        self.small_settings_button = FancyButton("Settings", self.first_row_x + self.small_button_width + self.spacing,
                                           HEIGHT // 2 - 50,
                                           self.small_button_width, self.small_button_height, BUTTON_COLOR, BUTTON_HOVER)

        # Quit button width is as wide as Resume + Settings buttons combined, centered below the first row
        self.small_quit_button = FancyButton("Quit", WIDTH // 2 - (self.small_button_width * 2 + self.spacing) // 2,
                                       HEIGHT // 2 + 100,
                                       self.small_button_width * 2 + self.spacing, self.small_button_height, BUTTON_COLOR,
                                       BUTTON_HOVER)

        # Settings screen
        self.fullscreen_radio = RadioButton(WIDTH // 2 - 100, HEIGHT // 2, "Fullscreen", is_checked=True)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.is_clicked():
                self.running = False
                self.start_game = True
            if self.settings_button.is_clicked():
                self.settings_game = True
                self.draw_menu()
            if self.quit_button.is_clicked():
                self.running = False
            if self.back_button.is_clicked():
                self.settings_game = False
                self.draw_menu()
            if self.fullscreen_radio.is_clicked(pygame.mouse.get_pos()):
                self.toggle_fullscreen()
                self.fullscreen_radio.is_checked = fullscreen
                self.draw_menu()
        # elif event.type == pygame.K_ESCAPE and self.start_game == True


    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((1280, 720))  # Default window size
    def draw_menu(self):
        self.screen.fill(BACKGROUND_COLOR)

        if not self.settings_game:
            # Draw main menu buttons
            self.start_button.draw(self.screen)
            self.settings_button.draw(self.screen)
            self.quit_button.draw(self.screen)
        else:
            # Draw settings screen
            self.fullscreen_radio.draw(self.screen)
            self.back_button.draw(self.screen)
