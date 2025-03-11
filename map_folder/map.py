import pygame



#find normal png's pls
tile_images = {
    0: pygame.image.load("map_folder/png/grass.png"),
    1: pygame.image.load("map_folder/png/water.jpg"),
    2: pygame.image.load("map_folder/png/path.jpg"),
}

game_map = [
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 2, 2, 2, 0],
    [0, 0, 1, 1, 0, 0, 2, 2, 2, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


def draw_map(screen, TILE_SIZE):
    for row_index, row in enumerate(game_map):
        for col_index, tile in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE

            if tile in tile_images:
                screen.blit(tile_images[tile], (x, y))
            else:
                pygame.draw.rect(screen, (255, 0, 0), (x, y, TILE_SIZE, TILE_SIZE))