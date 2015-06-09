#!/usr/bin/env python3
import unittest
import time
import random
import numpy
from main import GameOfLife

class TestGameOfLife(unittest.TestCase):

    def setUp(self):
        self.game_options = {
          'rows' : 25,
          'cols' : 35,
          'alive_cells' : 100
        }
        self.game = GameOfLife(self.game_options)

    def tearDown(self):
        self.game = None
        self.game_options = None
        
  
    def test_generation_number_is_set(self):
        """When the game is initialized. Generation count is set to 1."""
        self.assertEqual(self.game.generation, 1)

    def test_cells_are_initalized_with_correct_ammount(self):
        """"The user provides the amount of starting live cells in the game options. Check that is accurately conveyed to the real game."""
        alive_cells = 0
        for i, line in enumerate(self.game.current_cells):
            for j, cell in enumerate(line):
                if cell:
                    alive_cells += 1

        self.assertEqual(alive_cells, self.game_options['alive_cells'])

    def test_alive_neighbour_count(self):
        """Test that the amount of alive neighbours is being calculated properly."""
        self.game.current_cells = self.game.blank_cells.copy()
        self.game.current_cells[0][0] = 1
        self.game.current_cells[0][1] = 1

        self.assertEqual(self.game.alive_neighbours(0,0), 1)
        self.assertEqual(self.game.alive_neighbours(0,1), 1)
        self.assertEqual(self.game.alive_neighbours(0,2), 1)
        self.assertEqual(self.game.alive_neighbours(0,3), 0)
        self.assertEqual(self.game.alive_neighbours(1,0), 2)
        self.assertEqual(self.game.alive_neighbours(1,1), 2)
        self.assertEqual(self.game.alive_neighbours(1,2), 1)
        self.assertEqual(self.game.alive_neighbours(1,3), 0)




if __name__ == '__main__':
    unittest.main()