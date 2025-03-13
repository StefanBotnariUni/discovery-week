import streamlit as st
import pygame
import sys
from static_variables import *
from map_folder.map import Map
from Character.classes import Player
from MenuCode import Menu
from HeadMovements.hadle_head_move import get_head_direction, cap
import cv2
import numpy as np

pygame.init()

# Initialize screen
info = pygame.display.Info()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("PYCRAFT")
pygame.display.set_icon(pygame.image.load("images/favicon.png"))

# Create Menu
menu = Menu(screen)

# Streamlit setup
st.title('PyCraft Streaming Example')

# Function to capture, rotate, and flip PyGame screen
def capture_screen():
    frame = pygame.surfarray.array3d(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    frame = cv2.flip(frame, 1)  # Flip horizontally
    return frame

# Function to capture video feed from the camera
# Function to capture video feed from the camera
# Function to capture video feed from the camera
def capture_camera_feed():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Flip the frame horizontally if necessary
        frame = cv2.flip(frame, 1)  # 1 means flipping around the y-axis (horizontal flip)
        # Resize the camera feed
        frame = cv2.resize(frame, (200, 150))  # Resize the camera feed
    return frame

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

    # Create a placeholder for the image
    image_placeholder = st.empty()

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

        # Capture camera feed and overlay it on the top right of the screen
        camera_frame = capture_camera_feed()
        if camera_frame is not None:
            # Transpose the frame to fix the orientation
            camera_frame = cv2.transpose(camera_frame)  # Swap width and height
            camera_surface = pygame.surfarray.make_surface(camera_frame)
            screen.blit(camera_surface, (WIDTH - 210, 10))  # Position the camera feed on the top right

        pygame.display.flip()

        # Capture screen and display in Streamlit
        frame = capture_screen()
        image_placeholder.image(frame, channels="BGR", use_column_width=False)