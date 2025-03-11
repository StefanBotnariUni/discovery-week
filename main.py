import pygame
import sys
from static_variables import *
from map.map import draw_map

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_map(screen, TILE_SIZE)
    pygame.display.flip()


pygame.quit()
sys.exit()