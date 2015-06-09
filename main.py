#!/usr/bin/env python3
import time
import random
import numpy

class GameOfLife:
    """
        docstring for GameOfLife

        1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
        2. Any live cell with two or three live neighbours lives on to the next generation.
        3. Any live cell with more than three live neighbours dies, as if by overcrowding.
        4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """

    colors = {
        'green' : '\033[92m',
        'red' : '\033[91m',
        'end' : '\033[0m'
    }


    def __init__(self, options):
        self.generation = 1
        self.blank_cells = numpy.zeros((options['rows'], options['cols']), dtype=int)
        self.current_cells = self.blank_cells.copy()
        self.game_active = False

        for i in range(options['alive_cells']):
            self.toggle_cell(options)

    def toggle_cell(self, options):
        randX = random.randint(0, options['rows']-1)
        randY = random.randint(0, options['cols']-1)
        if self.current_cells[randX][randY]:
            self.toggle_cell(options)
        else:
            self.current_cells[randX][randY] = 1

    def start(self):
        self.draw_cells(self.current_cells)
        self.game_active = True
        try:
            while self.game_active:
                self.tick()
        except KeyboardInterrupt:
            print("\nGame Over. Thanks for playing!")


    def alive_neighbours(self, cellX, cellY):
        alive_neighbours = 0

        for x, row in enumerate(self.current_cells):
            for y, cell in enumerate(row):
                a = abs(x-cellX)
                b = abs(y-cellY)
                c = a <= 1
                d = b <= 1
                if ((c and d) and (a or b)) and not (a == 0 and b == 0):
                    # This cell is a neighbour
                    if cell:
                        # cell is alive
                        alive_neighbours += 1

        return alive_neighbours

    def update_cells(self):
        new_cells = self.blank_cells.copy()
        for i, line in enumerate(self.current_cells):
            for j, element in enumerate(line):
                alive_neighbours = self.alive_neighbours(i, j)

                if element:
                    # This element is alive
                    alive_text = 'alive'

                    if (alive_neighbours > 1) and (alive_neighbours < 4):
                        new_cells[i][j] = 1

                else:
                    if alive_neighbours == 3:
                        # Dead cell is now alive again
                        new_cells[i][j] = 1

        return new_cells

    def tick(self):
        self.generation += 1
        print('Calulating generation ' + str(self.generation))
        self.current_cells = self.update_cells()
        time.sleep(1)
        self.draw_cells(self.current_cells)
        

    def draw_cells(self, grid):

        for line in grid:
            string = ''
            for element in line:
                if element:
                    text = GameOfLife.colors['green'] + 'O' + GameOfLife.colors['end']
                else:
                    text = GameOfLife.colors['red'] + 'X' + GameOfLife.colors['end']
                string += text
            print(string)

if __name__ == "__main__":
    game = GameOfLife({'rows' : 25, 'cols' : 35, 'alive_cells' : 100})
    game.start()


        