import pygame
import os
import sys
from SpriteProcessor.SpriteSheetProcessor import SpriteSheetProcessor
import math


class Player:
    def __init__(self, x, y, speed, sprite_sheet_path, sprite_width, sprite_height, scale_factor=2):
        self.position = pygame.Vector2(x, y)
        self.speed = speed
        self.move_x = 0
        self.move_y = 0
        self.scale_factor = scale_factor

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

    def handle_input(self, keys):
        """Handle player movement based on keyboard input."""
        # Reset movement
        self.move_x = 0
        self.move_y = 0

        # Movement logic
        if keys[pygame.K_w]:
            self.move_y -= 1
        if keys[pygame.K_s]:
            self.move_y += 1
        if keys[pygame.K_a]:
            self.move_x -= 1
        if keys[pygame.K_d]:
            self.move_x += 1

        # Normalize movement vector if moving diagonally
        if self.move_x != 0 and self.move_y != 0:
            self.move_x /= math.sqrt(2)
            self.move_y /= math.sqrt(2)

    def update(self, dt):
        """Update the player's position based on movement and delta time."""
        self.position.x += self.move_x * self.speed * dt
        self.position.y += self.move_y * self.speed * dt
        self.rect.center = (int(self.position.x), int(self.position.y))  # Update rect position

    def draw(self, screen):
        """Draw the player on the screen."""
        screen.blit(self.image, self.rect)

    def get_movement(self):
        """Return the current movement vector for debugging or other purposes."""
        return self.move_x, self.move_y
