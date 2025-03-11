import pygame
import sys
from static_variables import *
from map_folder.map import Map
from Character.classes import Player
from MenuCode import Menu

pygame.init()

# Initialize screen
info = pygame.display.Info()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("PYCRAFT")

# Create Menu
menu = Menu(screen)

# Menu Loop (runs until the player starts the game)
while menu.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        menu.handle_event(event)

    menu.draw_menu()
    pygame.display.flip()

# After the menu is closed, start the game
if menu.start_game:  # Only proceed if the user starts the game

    game_map = Map(220)
    player = Player(x=400, y=300, speed=150, sprite_sheet_path="Character/png/character.png", sprite_width=32, sprite_height=32)

    # Game Loop
    clock = pygame.time.Clock()
    fps_limit = 60

    while True:  # Infinite loop for the game, exits on quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.handle_input(keys)

        dt = clock.tick(fps_limit) / 1000  # Delta time
        player.update(dt)

        # Draw game elements in order
        screen.fill((0, 0, 0))  # Clear screen first
        game_map.draw(screen)  # Draw the map first
        player.draw(screen)  # Draw the player on top

        pygame.display.flip()
