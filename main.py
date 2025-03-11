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
    player = Player(x=WIDTH/2, y=HEIGHT/2, speed=150, sprite_sheet_path="Character/png/character.png", sprite_width=32, sprite_height=32)

    # Game Loop
    clock = pygame.time.Clock()
    fps_limit = 60

    # Camera offset initialization
    camera_offset = pygame.Vector2(0, 0)

    while True:
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

        # Update camera offset based on the player's position
        camera_offset.x = WIDTH / 2 - player.position.x
        camera_offset.y = HEIGHT / 2 - player.position.y

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the map with camera offset
        game_map.draw(screen, camera_offset)

        # Draw the player at the center of the screen
        player.draw(screen)

        pygame.display.flip()

