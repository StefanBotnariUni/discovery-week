import pygame
pygame.font.init()
pygame.init()
CAPTION = 'game'
TILE_SIZE = 64

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
# Viewport dimensions
VIEWPORT_WIDTH = 960
VIEWPORT_HEIGHT = 540

# Colors (Minecraft-inspired)
BACKGROUND_COLOR = (100, 150, 100)  # Earthy green
BUTTON_COLOR = (34, 139, 34)  # Forest Green
BUTTON_HOVER = (24, 100, 24)  # Darker green for hover effect
WHITE = (255, 255, 255)
TEXT_COLOR = (200, 255, 200)  # Light greenish text

# Load and resize logo image
logo = pygame.image.load("images/pycraft_title.png")
logo = pygame.transform.scale(logo, (508, 91))

#colors
BLUE = (0, 0, 255)