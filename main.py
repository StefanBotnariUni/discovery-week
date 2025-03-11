import pygame
import sys
from static_variables import *
from map_folder.map import draw_map
from Character.classes import Character
from MenuCode import Menu

pygame.init()

info = pygame.display.Info()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("PYCRAFT")

menu = Menu(screen)

while menu.running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            menu.handle_event(event)

    menu.draw_menu()

    pygame.display.flip()

player = Character(400, 300)
while menu.start_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_runs = False
        player.handle_input(event)
    player.update()
    screen.fill((0, 0, 0))
    draw_map(screen, TILE_SIZE)
    player.draw(screen)
    pygame.display.flip()

pygame.quit()