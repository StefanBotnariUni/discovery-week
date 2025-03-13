import pygame


class Map:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.tile_images = {
            0: pygame.image.load("map_folder/png/grass_block_W.png").convert_alpha(),
            1: pygame.image.load("map_folder/png/tree_pine_S.png").convert_alpha(),  # Tree image
            2: pygame.image.load("map_folder/png/cliff_cornerInner_S.png").convert_alpha(),
        }
        self.background = pygame.image.load("Images/game_background.jpg").convert()

        self.surface_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.ground_map = [
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, 2],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, 2],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, 2],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, 2],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, 2],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        ]
        self.tree_layer = [
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, 1, -1],
            [-1, -1, -1, -1, 1, -1, -1, -1, -1, -1],
            [-1, 1, -1, -1, -1, -1, 1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, 1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        ]

    def draw_layer(self, screen, camera_offset, layer, x_offset=0, y_offset=0):
        """Draw a specific layer of the map using the tile images with camera offset and x/y offsets."""
        map_height = len(layer)
        map_width = len(layer[0]) if map_height > 0 else 0

        for row in range(map_height):
            for col in range(map_width):
                # Apply x and y offsets to the tile position
                x = (col - row) * (self.tile_size // 2) + camera_offset.x + x_offset
                y = (col + row) * (self.tile_size // 4) + camera_offset.y + y_offset

                tile = layer[row][col]
                if tile in self.tile_images:
                    screen.blit(self.tile_images[tile], (x, y))

    def draw(self, screen, camera_offset):
        """Draw the game map with background, ground, surface, and tree layers."""
        screen.blit(self.background, (0, 0))  # Draw background first
        self.draw_layer(screen, camera_offset, self.ground_map, x_offset=-4, y_offset=119)
        self.draw_layer(screen, camera_offset, self.surface_map)
        self.draw_layer(screen, camera_offset, self.tree_layer)
