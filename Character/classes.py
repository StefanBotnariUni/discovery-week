import pygame
import os
import sys
from SpriteProcessor.SpriteSheetProcessor import SpriteSheetProcessor
import math
import random
from static_variables import *

class Player:
    def __init__(self, x, y, speed, sprite_sheet_path, sprite_width, sprite_height, scale_factor=3):
        self.position = pygame.Vector2(x, y)
        self.speed = speed
        self.move_x = 0
        self.move_y = 0
        self.scale_factor = scale_factor
        self.frame_index = 0
        self.animation_speed = 0.1
        self.direction = None

        # Load the sprite sheet and extract sprites
        self.sprite_processor = SpriteSheetProcessor(sprite_sheet_path, sprite_width, sprite_height)
        self.sprites = self.sprite_processor.split_sprites()

        # Convert the first sprite from PIL to Pygame surface
        self.image = self.pil_to_pygame(self.sprites[0][0])

        # Upscale the image
        self.image = pygame.transform.scale(self.image,
                                            (sprite_width * scale_factor, sprite_height * scale_factor))
        self.rect = self.image.get_rect(center=(x, y))

    def pil_to_pygame(self, pil_image):
        """Convert a PIL image to a pygame surface."""
        return pygame.image.fromstring(pil_image.tobytes(), pil_image.size, pil_image.mode).convert_alpha()

    def change_image(self, direction):
        """Change the player's image based on movement direction."""
        self.direction = direction
        if direction == 1:  # up
            self.frame_index = (self.frame_index + self.animation_speed) % 3
            self.image = self.pil_to_pygame(self.sprites[3][int(self.frame_index)])
        elif direction == 2:  # down
            self.frame_index = (self.frame_index + self.animation_speed) % 3
            self.image = self.pil_to_pygame(self.sprites[0][int(self.frame_index)])
        elif direction == 3:  # left
            self.frame_index = (self.frame_index + self.animation_speed) % 3
            self.image = self.pil_to_pygame(self.sprites[1][int(self.frame_index)])
        elif direction == 4:  # right
            self.frame_index = (self.frame_index + self.animation_speed) % 3
            self.image = self.pil_to_pygame(self.sprites[2][int(self.frame_index)])

        # Upscale the image
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * self.scale_factor,
                                             self.image.get_height() * self.scale_factor))

    def handle_input(self, keys):
        """Handle player movement based on keyboard input."""
        # Reset movement
        self.move_x = 0
        self.move_y = 0

        # Movement logic
        if keys[pygame.K_w]:
            self.move_y -= 1
            self.change_image(1)  # up
        if keys[pygame.K_s]:
            self.move_y += 1
            self.change_image(2)  # down
        if keys[pygame.K_a]:
            self.move_x -= 1
            self.change_image(3)  # left
        if keys[pygame.K_d]:
            self.move_x += 1
            self.change_image(4)  # right

        # Normalize movement vector if moving diagonally
        if self.move_x != 0 and self.move_y != 0:
            self.move_x /= math.sqrt(2)
            self.move_y /= math.sqrt(2)

    def update(self, dt):
        """Update the player's position based on movement and delta time."""
        self.position.x += self.move_x * self.speed * dt
        self.position.y += self.move_y * self.speed * dt
        self.rect.center = (int(self.position.x), int(self.position.y))  # Update rect position

        # Update the animation frame if moving
        if self.move_x != 0 or self.move_y != 0:
            self.change_image(self.direction)

    def draw(self, screen):
        """Draw the player at the center of the screen."""
        screen.blit(self.image, (WIDTH // 2 - self.rect.width // 2, HEIGHT // 2 - self.rect.height // 2))

    def get_movement(self):
        """Return the current movement vector for debugging or other purposes."""
        return self.move_x, self.move_y