import pygame

class Map:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.tile_images = {
            0: pygame.image.load("map_folder/png/grass_block_W.png").convert_alpha(),
        }

        self.game_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def draw(self, screen, camera_offset):
        """Draw the game map using the tile images with camera offset."""
        map_height = len(self.game_map)
        map_width = len(self.game_map[0]) if map_height > 0 else 0

        for row in range(map_height):
            for col in range(map_width):
                x = (col - row) * (self.tile_size // 2) + camera_offset.x
                y = (col + row) * (self.tile_size // 4) + camera_offset.y

                tile = self.game_map[row][col]
                if tile in self.tile_images:
                    screen.blit(self.tile_images[tile], (x, y))