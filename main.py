import pygame
import sys
from static_variables import *
from map_folder.map import draw_map
from Character.classes import Character
from menu_code import Menu  # Assume the Menu class is imported from a module

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)

# Initialize game objects
player = Character(400, 300)
menu = Menu(screen)  # Create an instance of your Menu

# Game states
STATE_MENU = 0
STATE_GAME = 1
current_state = STATE_MENU

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Pass events to the current state handler
        if current_state == STATE_MENU:
            menu.handle_event(event)
        elif current_state == STATE_GAME:
            player.handle_input(event)

    # Update based on state
    if current_state == STATE_MENU:
        menu.update()
        if menu.start_game:  # Check if the menu's start button was clicked
            current_state = STATE_GAME
    elif current_state == STATE_GAME:
        player.update()

    # Draw based on state
    screen.fill((0, 0, 0))
    if current_state == STATE_MENU:
        menu.draw()
    elif current_state == STATE_GAME:
        draw_map(screen, TILE_SIZE)
        player.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()