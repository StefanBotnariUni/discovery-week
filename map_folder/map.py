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

    def draw(self, screen):
        """Draw the game map using the tile images in an isometric projection."""
        map_height = len(self.game_map)
        map_width = len(self.game_map[0]) if map_height > 0 else 0

        for row in range(map_height):
            for col in range(map_width):
                # Calculate the isometric position
                x = (col - row) * (self.tile_size // 2)
                y = (col + row) * (self.tile_size // 4)

                # Adjust the position to center the map on the screen
                x += screen.get_width() // 2
                y += screen.get_height() // 4

                tile = self.game_map[row][col]
                if tile in self.tile_images:
                    screen.blit(self.tile_images[tile], (x, y))
                else:
                    pygame.draw.rect(screen, (255, 0, 0), (x, y, self.tile_size, self.tile_size))