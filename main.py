import pygame
import sys
from static_variables import *
from map_folder.map import Map
from Character.classes import Player
from MenuCode import Menu
from HeadMovements.hadle_head_move import get_head_direction
import cv2

pygame.init()

# Initialize screen
info = pygame.display.Info()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("PYCRAFT")
pygame.display.set_icon(pygame.image.load("images/favicon.png"))

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

    # Initialize viewport dimensions (smaller resolution)
    viewport_width = VIEWPORT_WIDTH
    viewport_height = VIEWPORT_HEIGHT

    # Create a viewport surface (smaller resolution)
    viewport_surface = pygame.Surface((viewport_width, viewport_height))

    # Initialize game objects
    game_map = Map(220)
    player = Player(
        x=viewport_width // 2,  # Start player at the center of the viewport
        y=viewport_height // 2,
        speed=150,
        sprite_sheet_path="Character/png/character.png",
        sprite_width=32,
        sprite_height=32
    )

    # Game Loop
    clock = pygame.time.Clock()
    fps_limit = 60

    # Camera offset initialization
    camera_offset = pygame.Vector2(0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()  # Release the camera
                cv2.destroyAllWindows()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                cap.release()
                cv2.destroyAllWindows()
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:  # Handle screen resizing
                # Update screen dimensions
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)

        # Handle keyboard input
        keys = pygame.key.get_pressed()
        player.handle_input(keys)

        # Handle head movement
        head_dir = get_head_direction()
        player.handle_head_movement(head_dir)

        # Update game state
        dt = clock.tick(fps_limit) / 1000  # Delta time
        player.update(dt)

        # Update camera offset based on the player's position
        camera_offset.x = viewport_width // 2 - player.position.x
        camera_offset.y = viewport_height // 2 - player.position.y

        # Clear the viewport surface
        viewport_surface.fill((0, 0, 0))

        # Draw the map with camera offset
        game_map.draw(viewport_surface, camera_offset)

        # Draw the player at the center of the viewport
        player.draw(viewport_surface)

        # Scale the viewport surface to the screen size
        scaled_viewport = pygame.transform.scale(viewport_surface, (WIDTH, HEIGHT))

        # Draw the scaled viewport to the screen
        screen.blit(scaled_viewport, (0, 0))

        pygame.display.flip()