import numpy as np
import random
import pygame

class GameGrid:

    def __init__(self, width, height, cell_size):
        self.columns = int(height/cell_size)
        self.rows = int(width/cell_size)
        self.cell_size = cell_size
        self.grid_array = np.ndarray((self.rows, self.columns))
        self.generate_random()

    def generate_random(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0, 1)

    def new_generation(self):
        new_grid = np.ndarray((self.rows, self.columns))
        for x in range(self.rows):
            for y in range(self.columns):
                neighbors = 0

                # count neighbors
                for x_offset in range(-1, 2, 1):
                    for y_offset in range(-1, 2, 1):
                        if not(x_offset == 0 and y_offset == 0):
                            try:
                                neighbors += self.grid_array[x+x_offset][y+y_offset]
                            except:
                                neighbors += 0

                # game of life rules
                if self.grid_array[x][y] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[x][y] = 0
                    else:
                        new_grid[x][y] = 1
                else:
                    if neighbors == 3:
                        new_grid[x][y] = 1
                    else:
                        new_grid[x][y] = self.grid_array[x][y]

        self.grid_array = new_grid

    def draw_grid(self, screen, dead_color, live_color):
        for x in range(self.rows):
            for y in range(self.columns):
                color = dead_color
                if self.grid_array[x][y] == 1:
                    color = live_color

                pygame.draw.rect(screen, color,
                                 pygame.Rect(x*self.cell_size, y*self.cell_size, self.cell_size, self.cell_size))
