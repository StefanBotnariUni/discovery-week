import pygame
import sys
from static_variables import *
from map.map import draw_map
from Character.classes import Character


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)



player = Character(400, 300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.handle_input(event)


    player.update()


    screen.fill((0, 0, 0))
    draw_map(screen, TILE_SIZE)
    player.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()