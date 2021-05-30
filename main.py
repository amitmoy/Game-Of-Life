import pygame
import numpy as np
import GameGrid as game


pygame.init()
width = 1920
height = 1024
cell_size = 10
fps = 10
grid = game.GameGrid(width=width, height=height, cell_size=cell_size)
screen = pygame.display.set_mode([width, height])
running = True
clock = pygame.time.Clock()


while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(fps)

    screen.fill((50, 50, 50))

    grid.new_generation()

    grid.draw_grid(screen, (0, 0, 0), (255, 255, 255))

    pygame.display.update()

# Done! Time to quit.
pygame.quit()