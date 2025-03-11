import pygame
import sys

# Initialize Pygame and the font module explicitly
pygame.init()
pygame.font.init()  # Explicitly initialize the font module

# Define global constants for dimensions, colors, etc.
BACKGROUND_COLOR = (100, 150, 100)  # Earthy green
BUTTON_COLOR = (34, 139, 34)  # Forest Green
BUTTON_HOVER = (24, 100, 24)  # Darker green for hover effect
WHITE = (255, 255, 255)
TEXT_COLOR = (200, 255, 200)  # Light greenish text

# Font settings
font_path = "src/PressStart2P-Regular.ttf"
font = pygame.font.Font(font_path, 28)  # Button text font

class FancyButton:
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.base_color = color
        self.hover_color = hover_color
        self.color = color

    def draw(self, screen):
        # Check if the button is hovered over
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hover_color
        else:
            self.color = self.base_color

        # Draw the button
        pygame.draw.rect(screen, self.color, self.rect, border_radius=15)

        # Draw the text inside the button
        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.start_game = False  # Flag to check if start is clicked

        # Create buttons
        self.start_button = FancyButton("Start", 100, 100, 200, 50, BUTTON_COLOR, BUTTON_HOVER)
        self.settings_button = FancyButton("Settings", 100, 200, 200, 50, BUTTON_COLOR, BUTTON_HOVER)
        self.quit_button = FancyButton("Quit", 100, 300, 200, 50, BUTTON_COLOR, BUTTON_HOVER)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.is_clicked():
                self.start_game = True
            if self.settings_button.is_clicked():
                print("Settings clicked")  # Handle settings menu here
            if self.quit_button.is_clicked():
                self.running = False  # Quit the game

    def update(self):
        # Any update logic related to the menu can go here
        pass

    def draw(self):
        # Fill screen with background color
        self.screen.fill(BACKGROUND_COLOR)

        # Draw buttons
        self.start_button.draw(self.screen)
        self.settings_button.draw(self.screen)
        self.quit_button.draw(self.screen)

class Game:
    def __init__(self, screen):
        self.screen = screen
        # Initialize game components like player, map, etc.
        # Example: self.player = Player()

    def handle_event(self, event):
        # Handle events for the game
        pass

    def update(self):
        # Update game state (e.g., move player, update map, etc.)
        pass

    def draw(self):
        # Draw game components (e.g., player, map, etc.)
        self.screen.fill((0, 0, 0))  # Clear screen with black for now
        # Example: self.player.draw(self.screen)
        pygame.display.flip()

# Main game loop
def main():
    pygame.init()

    # Set up the screen
    info = pygame.display.Info()
    width, height = info.current_w, info.current_h
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("PyCraft")

    # Initialize the menu and game objects
    menu = Menu(screen)
    game = Game(screen)

    # Game state management
    current_state = 'menu'  # Start with the menu

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Pass events to the current state handler
            if current_state == 'menu':
                menu.handle_event(event)
            elif current_state == 'game':
                game.handle_event(event)

        # Update based on state
        if current_state == 'menu':
            menu.update()
            if menu.start_game:  # If the start button was clicked
                current_state = 'game'
        elif current_state == 'game':
            game.update()

        # Draw based on state
        if current_state == 'menu':
            menu.draw()
        elif current_state == 'game':
            game.draw()

        pygame.display.flip()  # Update the display

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
