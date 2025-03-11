import pygame
import sys
from static_variables import *
from map_folder.map import draw_map
from Character.classes import Player
from MenuCode import Menu

pygame.init()

info = pygame.display.Info()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("PYCRAFT")

menu = Menu(screen)

while menu.running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            menu.handle_event(event)

    menu.draw_menu()

    pygame.display.flip()

# Create a player object with an image
player = Player(x=400, y=300, speed=150, sprite_sheet_path="Character/png/character.png", sprite_width=32, sprite_height=32, scale_factor=3)
clock = pygame.time.Clock()
fps_limit = 60
while menu.start_game:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu.start_game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            menu.start_game = False

    # Get keyboard input
    keys = pygame.key.get_pressed()

    # Handle player input
    player.handle_input(keys)

    # Update player position
    dt = clock.tick(fps_limit) / 1000  # Delta time in seconds
    player.update(dt)

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the player
    player.draw(screen)

    # Render the movement vector text
    move_x, move_y = player.get_movement()
    text_surface = font.render(f'[{move_x:.2f}, {move_y:.2f}]', True, (0, 0, 0))
    screen.blit(text_surface, (50, 50))

    # Update the display
    pygame.display.flip()

pygame.quit()