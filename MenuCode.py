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
        # Load original background image and scale it to current screen size
        self.original_background = pygame.image.load("images/background.png")
        self.background_image = pygame.transform.scale(self.original_background, self.screen.get_size())
        self.button_width = 300
        self.button_height = 90
        self.spacing = 40
        self.fullscreen = True
        self.total_width = (3 * self.button_width) + (2 * self.spacing)
        self.start_x = (self.screen.get_width() - self.total_width) // 2
        self.start_y = self.screen.get_height() // 2
        self.small_button_width = int(self.button_width * 0.8)
        self.small_button_height = int(self.button_height * 0.8)
        self.first_row_width = self.small_button_width * 2 + self.spacing
        # Calculate the starting X position to center the buttons (taking the combined width into account)
        self.first_row_x = self.screen.get_width() // 2 - self.first_row_width // 2
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
            (self.screen.get_width() - self.button_width) // 2,  # Centered horizontally
            self.screen.get_height() - self.button_height - 50,  # Slightly higher from the bottom
            self.button_width,
            self.button_height,
            BUTTON_COLOR,
            BUTTON_HOVER
        )
        self.small_resume_button = FancyButton("Resume", self.first_row_x, self.screen.get_height() // 2 - 50, self.small_button_width,
                                         self.small_button_height,
                                         BUTTON_COLOR, BUTTON_HOVER)
        self.small_settings_button = FancyButton("Settings", self.first_row_x + self.small_button_width + self.spacing,
                                           self.screen.get_height() // 2 - 50,
                                           self.small_button_width, self.small_button_height, BUTTON_COLOR, BUTTON_HOVER)

        # Quit button width is as wide as Resume + Settings buttons combined, centered below the first row
        self.small_quit_button = FancyButton("Quit", self.screen.get_width() // 2 - (self.small_button_width * 2 + self.spacing) // 2,
                                       self.screen.get_height() // 2 + 100,
                                       self.small_button_width * 2 + self.spacing, self.small_button_height, BUTTON_COLOR,
                                       BUTTON_HOVER)

        # Settings screen
        self.fullscreen_radio = RadioButton(self.screen.get_width() // 2 - 100, self.screen.get_height() // 2, "Fullscreen", is_checked=True)

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
                self.fullscreen_radio.is_checked = self.fullscreen
                self.draw_menu()

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((1280, 720))

        # Update background to new screen dimensions
        self.background_image = pygame.transform.scale(self.original_background, self.screen.get_size())

        # Recalculate button positions after screen change
        self.reposition_buttons()

    def reposition_buttons(self):
        """Recalculates button positions when screen size changes"""
        self.button_width = int(self.screen.get_width() * 0.2)
        self.button_height = int(self.screen.get_height() * 0.1)
        self.spacing = int(self.screen.get_height() * 0.03)  # Adjust spacing based on screen height

        # Center horizontally
        center_x = (self.screen.get_width() - self.button_width) // 2

        # Position buttons in a vertical stack
        self.start_y = self.screen.get_height() // 3  # Start higher on the screen
        self.start_button.rect.topleft = (center_x, self.start_y)
        self.settings_button.rect.topleft = (center_x, self.start_y + self.button_height + self.spacing)
        self.quit_button.rect.topleft = (center_x, self.start_y + 2 * (self.button_height + self.spacing))

        # Position Back button correctly at the bottom
        self.back_button.rect.topleft = (
        center_x, self.screen.get_height() - self.button_height - int(self.screen.get_height() * 0.05))

        # Correctly update the radio button position (since it doesn't have a rect)
        self.fullscreen_radio.x = self.screen.get_width() // 2 - 100
        self.fullscreen_radio.y = self.screen.get_height() // 2

        self.draw_menu()  # Redraw the menu with updated button positions

    def draw_menu(self):
        self.screen.blit(self.background_image, (0, 0))

        if not self.settings_game:
            # Draw main menu buttons
            self.start_button.draw(self.screen)
            self.settings_button.draw(self.screen)
            self.quit_button.draw(self.screen)
        else:
            # Draw settings screen
            self.fullscreen_radio.draw(self.screen)
            self.back_button.draw(self.screen)