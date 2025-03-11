import pygame
import os
import sys

class Character:
    def __init__(self, x, y, width=64, height=64):
        image_path = 'Character/png/character.png'
        try:
            self.original_image = pygame.image.load(os.path.join(image_path))
            self.image = pygame.transform.scale(self.original_image, (width, height))
        except FileNotFoundError:
            print(f"Error: Image not found at {image_path}")
            pygame.quit()
            sys.exit()
        self.rect = self.image.get_rect()

        self.speed = 50
        self.direction = pygame.math.Vector2(0,0)
        self.facing = 'down'
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False



            # for animation
    #     self.animation_frames = {}
    #     self.load_animations()
    #     self.current_frame = 0
    #     self.animation_speed = 0.15
    #     self.last_update = pygame.time.get_ticks()
    #
    # def load_animations(self):
    #     directions = ["down", "up", "left", "right"]
    #     for direction in directions:
    #         self.animation_frames[direction] = [
    #             pygame.image.load(f"Character/animation/{direction}_{i}.png")
    #             for i in range(1, 5)  # Assuming 4 frames per direction
    #         ]
    # def animate(self):
    #     """Handle character animation"""
    #     now = pygame.time.get_ticks()
    #     if now - self.last_update > self.animation_speed * 1000:
    #         self.last_update = now
    #         self.current_frame = (self.current_frame + 1) % len(self.animation_frames[self.facing])
    #         self.image = self.animation_frames[self.facing][self.current_frame]

    def move(self):
        """Move character based on movement flags"""
        if self.moving_left:
            self.rect.x -= self.speed
        if self.moving_right:
            self.rect.x += self.speed
        if self.moving_up:
            self.rect.y -= self.speed
        if self.moving_down:
            self.rect.y += self.speed

    def update(self):
        """Update character state"""
        self.move()

    def draw(self, surface):
        """Draw character on the screen"""
        surface.blit(self.image, self.rect)

    def handle_input(self, event):
        """Handle keyboard input for movement"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.moving_left = True
            if event.key == pygame.K_d:
                self.moving_right = True
            if event.key == pygame.K_w:
                self.moving_up = True
            if event.key == pygame.K_s:
                self.moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.moving_left = False
            if event.key == pygame.K_d:
                self.moving_right = False
            if event.key == pygame.K_w:
                self.moving_up = False
            if event.key == pygame.K_s:
                self.moving_down = False