from PIL import Image
import numpy as np

class SpriteSheetProcessor:
    def __init__(self, image_path, sprite_width, sprite_height):
        self.image = Image.open(image_path)
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height
        self.sprites = []

    def split_sprites(self):
        img_width, img_height = self.image.size
        rows = img_height // self.sprite_height
        cols = img_width // self.sprite_width

        self.sprites = [[None for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                left = col * self.sprite_width
                upper = row * self.sprite_height
                right = left + self.sprite_width
                lower = upper + self.sprite_height

                sprite = self.image.crop((left, upper, right, lower))
                self.sprites[row][col] = sprite

        return self.sprites

    def get_sprite(self, row, col):
        if 0 <= row < len(self.sprites) and 0 <= col < len(self.sprites[0]):
            return self.sprites[row][col]
        return None