from unittest import TestCase
import sudoku


class MyTests(TestCase):
    def test_grid_to_set(self):
        grid_3 = [[7, 0, 0],
                  [6, 0, 0],
                  [9, 3, 0]]

        grid3_as_sets = [[{7}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}],
                         [{6}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}],
                         [{9}, {3}, {1, 2, 3, 4, 5, 6, 7, 8, 9}]]

        self.assertTrue(grid3_as_sets == sudoku.convertToSets(grid_3))

    # def test_convertToSets(self):
    #     self.fail()


