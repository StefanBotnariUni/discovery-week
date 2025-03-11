import pygame
import sys

# Initialize Pygame
pygame.init()

# Load a blockier font (Press Start 2P or any blocky font of your choice)
font_path = "src/PressStart2P-Regular.ttf"  # Change the path if you have it elsewhere
small_font_path = "src/PressStart2P-Regular.ttf"  # For smaller text
font = pygame.font.Font(font_path, 28)  # Adjusted button text size to be 20% smaller again
small_font = pygame.font.Font(small_font_path, 40)  # For other small text
fullscreen_font = pygame.font.Font(small_font_path, 15)  # For fullscreen label, adjusted to 15
settings_title_font = pygame.font.Font(small_font_path, 40)  # For Settings header, increased to 40px

# Get the largest possible screen resolution
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
fullscreen = True  # Start in fullscreen mode
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("PyCraft")  # Updated caption

# Colors (Minecraft-inspired)
BACKGROUND_COLOR = (100, 150, 100)  # Earthy green
BUTTON_COLOR = (34, 139, 34)  # Forest Green
BUTTON_HOVER = (24, 100, 24)  # Darker green for hover effect
WHITE = (255, 255, 255)
TEXT_COLOR = (200, 255, 200)  # Light greenish text

# Load and resize logo image
logo = pygame.image.load("images/pycraft_title.png")
logo = pygame.transform.scale(logo, (508, 91))


# Fancy button class
class FancyButton:
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.base_color = color
        self.hover_color = hover_color
        self.color = color
        self.alpha = 255  # Transparency for animation

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover_color
        else:
            self.color = self.base_color

        # Button shape
        pygame.draw.rect(screen, self.color, self.rect, border_radius=15)

        # Render text
        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())


# Radio button class
class RadioButton:
    def __init__(self, x, y, text, is_checked=False):
        self.x = x
        self.y = y
        self.text = text
        self.is_checked = is_checked
        self.radius = 15  # Radio button size

    def draw(self, screen):
        # Outer circle
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius, 2)

        # Inner filled circle (if checked)
        if self.is_checked:
            pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius // 2)

        # Render text
        text_surf = small_font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(midleft=(self.x + 25, self.y))
        screen.blit(text_surf, text_rect)

    def is_clicked(self, mouse_pos):
        return (mouse_pos[0] - self.x) ** 2 + (mouse_pos[1] - self.y) ** 2 <= self.radius ** 2


# Function to toggle fullscreen
def toggle_fullscreen():
    global fullscreen, screen
    fullscreen = not fullscreen
    if fullscreen:
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((1280, 720))  # Default window size


# Function to display the main menu
def main_menu():
    global running, in_main_menu
    while running:
        if in_main_menu:  # If we're in the main menu, show the menu
            screen.fill(BACKGROUND_COLOR)

            # Draw logo
            screen.blit(logo, ((WIDTH - logo.get_width()) // 2, HEIGHT // 4 - 50))

            # Draw buttons
            start_button.draw(screen)
            settings_button.draw(screen)
            quit_button.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.is_clicked():
                        start_game()  # Start the new game screen
                    if settings_button.is_clicked():
                        settings_menu()  # Go to settings menu
                    if quit_button.is_clicked():
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
        else:
            # If not in the main menu, run the game or the pause menu
            start_game()

# Function to start the game (new blank window)
def start_game():
    global game_paused
    game_running = True
    while game_running:
        screen.fill((0, 0, 0))  # Black screen for the game (could be replaced with your game content)

        if game_paused:
            pause_menu()  # Display pause menu if the game is paused
        else:
            # Placeholder text when game is running
            game_text = font.render("Game is Running!", True, WHITE)
            screen.blit(game_text, (WIDTH // 2 - game_text.get_width() // 2, HEIGHT // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_paused = not game_paused  # Toggle the pause state

        pygame.display.flip()

    pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)  # Restore fullscreen after game ends

# Function to display the pause menu
def pause_menu():
    global game_paused, in_main_menu

    # Make the buttons 20% smaller
    small_button_width = int(button_width * 0.8)
    small_button_height = int(button_height * 0.8)

    # Calculate the total width for the first row (Resume + Settings buttons + spacing between them)
    first_row_width = small_button_width * 2 + spacing

    # Calculate the starting X position to center the buttons (taking the combined width into account)
    first_row_x = WIDTH // 2 - first_row_width // 2  # Centering the first row of buttons

    # Create new buttons with smaller dimensions and properly centered
    resume_button = FancyButton("Resume", first_row_x, HEIGHT // 2 - 50, small_button_width, small_button_height,
                                BUTTON_COLOR, BUTTON_HOVER)
    settings_button = FancyButton("Settings", first_row_x + small_button_width + spacing, HEIGHT // 2 - 50,
                                  small_button_width, small_button_height, BUTTON_COLOR, BUTTON_HOVER)

    # Quit button width is as wide as Resume + Settings buttons combined, centered below the first row
    quit_button = FancyButton("Quit", WIDTH // 2 - (small_button_width * 2 + spacing) // 2, HEIGHT // 2 + 100,
                              small_button_width * 2 + spacing, small_button_height, BUTTON_COLOR, BUTTON_HOVER)

    # Pause menu background
    pygame.draw.rect(screen, (50, 50, 50), (WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2), border_radius=20)

    # Draw buttons
    resume_button.draw(screen)
    settings_button.draw(screen)
    quit_button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_paused = False
            in_main_menu = True  # Transition to main menu when quitting
        if event.type == pygame.MOUSEBUTTONDOWN:
            if resume_button.is_clicked():
                game_paused = False  # Resume the game
            if settings_button.is_clicked():
                settings_menu()  # Go to settings menu
            if quit_button.is_clicked():
                game_paused = False
                main_menu() # Go to main menu

# Function to display the settings menu
def settings_menu():
    global fullscreen
    in_settings = True

    fullscreen_radio = RadioButton(WIDTH // 2 - 150, HEIGHT // 2, "", fullscreen)

    while in_settings:
        screen.fill((80, 120, 80))  # Slightly darker green for settings background

        # Draw settings title with the updated font size (increased by 40%)
        title_surf = settings_title_font.render("Settings", True, WHITE)
        title_rect = title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(title_surf, title_rect)

        # Draw fullscreen option label
        fullscreen_text = fullscreen_font.render("Fullscreen", True, TEXT_COLOR)
        screen.blit(fullscreen_text, (WIDTH // 2 - 100, HEIGHT // 2 - 10))

        # Draw settings options
        fullscreen_radio.draw(screen)
        back_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_settings = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if fullscreen_radio.is_clicked(pygame.mouse.get_pos()):
                    toggle_fullscreen()
                    fullscreen_radio.is_checked = fullscreen  # Update radio button state
                if back_button.is_clicked():
                    in_settings = False  # Return to main menu

        pygame.display.flip()


# Button sizes
button_width, button_height = 300, 90
spacing = 40
total_width = (3 * button_width) + (2 * spacing)
start_x = (WIDTH - total_width) // 2
start_y = HEIGHT // 2

# Create buttons
start_button = FancyButton("Start", start_x, start_y, button_width, button_height, BUTTON_COLOR, BUTTON_HOVER)
settings_button = FancyButton("Settings", start_x + button_width + spacing, start_y, button_width, button_height,
                              BUTTON_COLOR, BUTTON_HOVER)
quit_button = FancyButton("Quit", start_x + (2 * button_width) + (2 * spacing), start_y, button_width, button_height,
                          BUTTON_COLOR, BUTTON_HOVER)
resume_button = FancyButton("Resume", WIDTH // 2 - 150, HEIGHT // 2 - 40, 300, 90, BUTTON_COLOR, BUTTON_HOVER)
back_button = FancyButton("Back", WIDTH // 2 - 150, HEIGHT // 2 + 80, 300, 90, BUTTON_COLOR, BUTTON_HOVER)

# Define global variable in_main_menu
in_main_menu = True

# Run the main menu
game_paused = False
running = True
main_menu()

pygame.quit()
sys.exit()