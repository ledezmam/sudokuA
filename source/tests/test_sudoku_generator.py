"""
Author: Maria Ledezma
Creation Date: 07/11/2013
"""
import unittest 
import sys 
sys.path.append( '../libs' ) 
from sudoku_generator import SudokuGenerator
from backtraking_algorithm import BacktrakingAlgorithm 

class TestSudokuGenerator(unittest.TestCase): 
    def setUp(self):
    	self.test_generator = SudokuGenerator()
    
    def test_is_valid_row_returns_false_when_duplicated_in_the_row_0(self):
    	self.test_generator.board_list =[[1, 4, 4, 3, 5, 6, 7, 8, 9],
    									 [2, 3, 5, 4, 6, 7, 8, 9, 1],
    									 [3, 5, 6, 7, 4, 8, 9, 1, 2],
    									 [4, 6, 7, 8, 9, 1, 2, 3, 5],
    									 [5, 7, 8, 9, 1, 2, 3, 4, 6],
    									 [6, 8, 9, 1, 2, 3, 4, 5, 7],
    									 [7, 9, 1, 2, 3, 4, 5, 6, 8],
    									 [8, 1, 2, 3, 4, 5, 6, 7, 9],
    									 [9, 2, 3, 4, 5, 6, 7, 8, 1]]

    	self.assertFalse(self.test_generator.is_valid_row(0))

    def test_is_valid_row_returns_false_when_duplicated_in_middle_row(self):
    	self.test_generator.board_list =[[1, 2, 4, 3, 5, 6, 7, 8, 9],
    									 [2, 3, 5, 4, 6, 7, 8, 9, 1],
    									 [3, 5, 6, 7, 4, 8, 9, 1, 2],
    									 [4, 6, 7, 8, 9, 1, 2, 3, 5],
    									 [5, 7, 8, 9, 1, 2, 5, 4, 6],
    									 [6, 8, 9, 1, 2, 3, 4, 5, 7],
    									 [7, 9, 1, 2, 3, 4, 5, 6, 8],
    									 [8, 1, 2, 3, 4, 5, 6, 9, 9],
    									 [9, 2, 3, 4, 5, 6, 8, 8, 1]]

    	self.assertFalse(self.test_generator.is_valid_row(4))

    def test_is_valid_row_returns_true_when_no_duplicate_in_row_0(self):
        self.test_generator.board_list =[[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                         [2, 3, 5, 4, 6, 7, 8, 9, 1],
                                         [3, 5, 6, 7, 4, 8, 9, 1, 2],
                                         [4, 6, 7, 8, 9, 1, 2, 3, 5],
                                         [5, 7, 8, 9, 1, 2, 5, 4, 6],
                                         [6, 8, 9, 1, 2, 3, 4, 5, 7],
                                         [7, 9, 1, 2, 3, 4, 5, 6, 8],
                                         [8, 1, 2, 3, 4, 5, 6, 9, 9],
                                         [9, 2, 3, 4, 5, 6, 8, 8, 1]]

        self.assertTrue(self.test_generator.is_valid_row(0))

    def test_is_valid_row_returns_true_when_no_duplicate_in_last_row(self):
        self.test_generator.board_list =[[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                         [2, 3, 5, 4, 6, 7, 8, 9, 1],
                                         [3, 5, 6, 7, 4, 8, 9, 1, 2],
                                         [4, 6, 7, 8, 9, 1, 2, 3, 5],
                                         [5, 7, 8, 9, 1, 2, 5, 4, 6],
                                         [6, 8, 9, 1, 2, 3, 4, 5, 7],
                                         [7, 9, 1, 2, 3, 4, 5, 6, 8],
                                         [8, 1, 2, 3, 4, 5, 6, 9, 9],
                                         [9, 2, 3, 4, 5, 6, 8, 7, 1]]

        self.assertTrue(self.test_generator.is_valid_row(8))

    def test_is_valid_col_returns_false_when_duplicate_in_col_0(self):
        self.test_generator.board_list =[[9, 2, 3, 4, 5, 6, 7, 8, 9],
                                         [2, 3, 5, 4, 6, 7, 8, 9, 1],
                                         [3, 5, 6, 7, 4, 8, 9, 1, 2],
                                         [4, 6, 7, 8, 9, 1, 2, 3, 5],
                                         [5, 7, 8, 9, 1, 2, 5, 4, 6],
                                         [6, 8, 9, 1, 2, 3, 4, 5, 7],
                                         [7, 9, 1, 2, 3, 4, 5, 6, 8],
                                         [8, 1, 2, 3, 4, 5, 6, 9, 9],
                                         [9, 2, 3, 4, 5, 6, 8, 7, 1]]

        self.assertFalse(self.test_generator.is_valid_col(0))

    def test_is_valid_col_returns_false_when_duplicate_in_last_col(self):
        self.test_generator.board_list =[[9, 2, 3, 4, 5, 6, 7, 8, 3],
                                         [2, 3, 5, 4, 6, 7, 8, 9, 1],
                                         [3, 5, 6, 7, 4, 8, 9, 1, 2],
                                         [4, 6, 7, 8, 9, 1, 2, 3, 5],
                                         [5, 7, 8, 9, 1, 2, 5, 4, 6],
                                         [6, 8, 9, 1, 2, 3, 4, 5, 7],
                                         [7, 9, 1, 2, 3, 4, 5, 6, 1],
                                         [8, 1, 2, 3, 4, 5, 6, 9, 9],
                                         [9, 2, 3, 4, 5, 6, 8, 7, 8]]

        self.assertFalse(self.test_generator.is_valid_col(8))

    def test_is_valid_col_returns_true_when_no_duplicate_in_col_0(self):
        self.test_generator.board_list =[[9, 2, 3, 4, 5, 6, 7, 8, 3],
                                         [2, 3, 5, 4, 6, 7, 8, 9, 1],
                                         [3, 5, 6, 7, 4, 8, 9, 1, 2],
                                         [4, 6, 7, 8, 9, 1, 2, 3, 5],
                                         [5, 7, 8, 9, 1, 2, 5, 4, 6],
                                         [6, 8, 9, 1, 2, 3, 4, 5, 7],
                                         [7, 9, 1, 2, 3, 4, 5, 6, 1],
                                         [8, 1, 2, 3, 4, 5, 6, 9, 9],
                                         [1, 2, 3, 4, 5, 6, 8, 7, 8]]

        self.assertTrue(self.test_generator.is_valid_col(0))

    def test_is_valid_col_returns_true_when_no_duplicate_in_col_7(self):
        self.test_generator.board_list =[[9, 2, 3, 4, 5, 6, 7, 8, 3],
                                         [2, 3, 5, 4, 6, 7, 8, 9, 1],
                                         [3, 5, 6, 7, 4, 8, 9, 1, 2],
                                         [4, 6, 7, 8, 9, 1, 2, 3, 5],
                                         [5, 7, 8, 9, 1, 2, 5, 4, 6],
                                         [6, 8, 9, 1, 2, 3, 4, 5, 7],
                                         [7, 9, 1, 2, 3, 4, 5, 6, 1],
                                         [8, 1, 2, 3, 4, 5, 6, 2, 9],
                                         [1, 2, 3, 4, 5, 6, 8, 7, 8]]

        self.assertTrue(self.test_generator.is_valid_col(7))

    def test_is_valid_square_returns_false_when_duplicate_in_square_0(self):
        self.test_generator.board_list =[[6, 5, 7, 1, 8, 4, 3, 2, 9],
                                         [9, 6, 8, 7, 3, 6, 4, 1, 5],
                                         [4, 3, 1, 2, 9, 5, 7, 6, 8],
                                         [2, 8, 6, 3, 5, 9, 1, 4, 7],
                                         [7, 9, 5, 4, 2, 1, 8, 3, 6],
                                         [3, 1, 4, 8, 6, 7, 5, 9, 2],
                                         [8, 7, 9, 6, 1, 3, 2, 5, 4],
                                         [1, 6, 2, 5, 4, 8, 9, 7, 3],
                                         [5, 4, 3, 9, 7, 2, 6, 8, 1]]

        self.assertFalse(self.test_generator.is_valid_square(0))

    def test_is_valid_square_returns_false_when_duplicate_in_last_square(self):
        self.test_generator.board_list =[[6, 5, 7, 1, 8, 4, 3, 2, 9],
                                         [9, 6, 8, 7, 3, 6, 4, 1, 5],
                                         [4, 3, 1, 2, 9, 5, 7, 6, 8],
                                         [2, 8, 6, 3, 5, 9, 1, 4, 7],
                                         [7, 9, 5, 4, 2, 1, 8, 3, 6],
                                         [3, 1, 4, 8, 6, 7, 5, 9, 2],
                                         [8, 7, 9, 6, 1, 3, 2, 5, 4],
                                         [1, 6, 2, 5, 4, 8, 7, 7, 3],
                                         [5, 4, 3, 9, 7, 2, 6, 8, 1]]

        self.assertFalse(self.test_generator.is_valid_square(8))

    def test_is_valid_square_returns_true_when_no_duplicate_in_square_0(self):
        self.test_generator.board_list =[[6, 5, 7, 1, 8, 4, 3, 2, 9],
                                         [9, 2, 8, 7, 3, 6, 4, 1, 5],
                                         [4, 3, 1, 2, 9, 5, 7, 6, 8],
                                         [2, 8, 6, 3, 5, 9, 1, 4, 7],
                                         [7, 9, 5, 4, 2, 1, 8, 3, 6],
                                         [3, 1, 4, 8, 6, 7, 5, 9, 2],
                                         [8, 7, 9, 6, 1, 3, 2, 5, 4],
                                         [1, 6, 2, 5, 4, 8, 9, 7, 3],
                                         [5, 4, 3, 9, 7, 2, 6, 8, 1]]

        self.assertTrue(self.test_generator.is_valid_square(0))

    def test_is_valid_square_returns_true_when_no_duplicate_in_last_square(self):
        self.test_generator.board_list =[[6, 5, 7, 1, 8, 4, 3, 2, 9],
                                         [9, 2, 8, 7, 3, 6, 4, 1, 5],
                                         [4, 3, 1, 2, 9, 5, 7, 6, 8],
                                         [2, 8, 6, 3, 5, 9, 1, 4, 7],
                                         [7, 9, 5, 4, 2, 1, 8, 3, 6],
                                         [3, 1, 4, 8, 6, 7, 5, 9, 2],
                                         [8, 7, 9, 6, 1, 3, 2, 5, 4],
                                         [1, 6, 2, 5, 4, 8, 9, 7, 3],
                                         [5, 4, 3, 9, 7, 2, 6, 8, 1]]

        self.assertTrue(self.test_generator.is_valid_square(8))

    def test_is_valid_board_returns_true_when_no_duplicate_in_sudoku_board(self):
        self.test_generator.board_list =[[6, 5, 7, 1, 8, 4, 3, 2, 9],
                                         [9, 2, 8, 7, 3, 6, 4, 1, 5],
                                         [4, 3, 1, 2, 9, 5, 7, 6, 8],
                                         [2, 8, 6, 3, 5, 9, 1, 4, 7],
                                         [7, 9, 5, 4, 2, 1, 8, 3, 6],
                                         [3, 1, 4, 8, 6, 7, 5, 9, 2],
                                         [8, 7, 9, 6, 1, 3, 2, 5, 4],
                                         [1, 6, 2, 5, 4, 8, 9, 7, 3],
                                         [5, 4, 3, 9, 7, 2, 6, 8, 1]]

        self.assertTrue(self.test_generator.is_valid_board())

    def test_is_valid_board_returns_false_when_duplicates_in_sudoku_board(self):
        self.test_generator.board_list =[[1, 4, 4, 3, 5, 6, 7, 8, 9],
                                         [2, 3, 5, 4, 6, 7, 8, 9, 1],
                                         [3, 5, 6, 7, 4, 8, 9, 1, 2],
                                         [4, 6, 7, 8, 9, 1, 2, 3, 5],
                                         [5, 7, 8, 9, 1, 2, 3, 4, 6],
                                         [6, 8, 9, 1, 2, 3, 4, 5, 7],
                                         [7, 9, 1, 2, 3, 4, 5, 6, 8],
                                         [8, 1, 2, 3, 4, 5, 6, 7, 9],
                                         [9, 2, 3, 4, 5, 6, 7, 8, 1]]

        self.assertFalse(self.test_generator.is_valid_board())

    def test_get_positions_returns_a_list_with_positions(self):
        exp_positions = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0),
                         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1),
                         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2),
                         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
                         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                         (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
                         (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6),
                         (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
                         (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)]

        self.assertEquals(exp_positions, self.test_generator.get_positions(9))

    def test_search_returns_true_if_valid_sudoku_was_generated(self):
        positions = self.test_generator.get_positions(9)
        valid_board = self.test_generator.search(positions,0)
        expected_valid_status = True
        self.assertEquals(expected_valid_status, valid_board)

    def test_generate_random_positions_does_not_return_an_empty_list(self):
        size_list = 4
        list_positions = self.test_generator.generate_random_positions(size_list)
        self.assertEquals(size_list, len(list_positions))

    def test_get_board_format_to_string_returns_multiline_string_format_when_board_numeric(self):
        board_to_format = [[1, 4, 4, 3, 5, 6, 7, 8, 9],
                           [2, 3, 5, 4, 6, 7, 8, 9, 1],
                           [3, 5, 6, 7, 4, 8, 9, 1, 2],
                           [4, 6, 7, 8, 9, 1, 2, 3, 5],
                           [5, 7, 8, 9, 1, 2, 3, 4, 6],
                           [6, 8, 9, 1, 2, 3, 4, 5, 7],
                           [7, 9, 1, 2, 3, 4, 5, 6, 8],
                           [8, 1, 2, 3, 4, 5, 6, 7, 9],
                           [9, 2, 3, 4, 5, 6, 7, 8, 1]]
        expected_board_string = "144356789\n" + \
                                "235467891\n" + \
                                "356748912\n" + \
                                "467891235\n" + \
                                "578912346\n" + \
                                "689123457\n" + \
                                "791234568\n" + \
                                "812345679\n" + \
                                "923456781\n"
        current_board_string = self.test_generator.get_board_format_to_string(board_to_format)
        self.assertEquals(expected_board_string, current_board_string)

    def test_get_board_format_to_string_returns_multiline_string_format_when_board_string(self):
        board_to_format = [['1', '.', '.', '5', '4', '9', '6', '8', '3'],
                           ['6', '4', '5', '.', '.', '3', '2', '.', '9'],
                           ['.', '8', '9', '2', '6', '1', '7', '4', '.'],
                           ['4', '.', '.', '.', '.', '.', '.', '5', '1'],
                           ['8', '1', '3', '4', '5', '6', '.', '.', '.'],
                           ['2', '5', '7', '1', '.', '.', '4', '3', '6'],
                           ['9', '6', '4', '.', '1', '5', '3', '2', '8'],
                           ['7', '3', '.', '.', '8', '2', '5', '9', '4'],
                           ['.', '2', '.', '9', '3', '4', '1', '6', '7']]
        expected_board_string = "1..549683\n" + \
                                "645..32.9\n" + \
                                ".8926174.\n" + \
                                "4......51\n" + \
                                "813456...\n" + \
                                "2571..436\n" + \
                                "964.15328\n" + \
                                "73..82594\n" + \
                                ".2.934167\n"
        current_board_string = self.test_generator.get_board_format_to_string(board_to_format)
        self.assertEquals(expected_board_string, current_board_string)

    def test_get_board_format_to_print_returns_format_by_quadrant(self):
        board_to_format = [['1', '.', '.', '5', '4', '9', '6', '8', '3'],
                           ['6', '4', '5', '.', '.', '3', '2', '.', '9'],
                           ['.', '8', '9', '2', '6', '1', '7', '4', '.'],
                           ['4', '.', '.', '.', '.', '.', '.', '5', '1'],
                           ['8', '1', '3', '4', '5', '6', '.', '.', '.'],
                           ['2', '5', '7', '1', '.', '.', '4', '3', '6'],
                           ['9', '6', '4', '.', '1', '5', '3', '2', '8'],
                           ['7', '3', '.', '.', '8', '2', '5', '9', '4'],
                           ['.', '2', '.', '9', '3', '4', '1', '6', '7']]
        expected_board_print = " 1 . . | 5 4 9 | 6 8 3 \n" + \
                               " 6 4 5 | . . 3 | 2 . 9 \n" + \
                               " . 8 9 | 2 6 1 | 7 4 . \n" + \
                               " - - - + - - - + - - -\n" + \
                               " 4 . . | . . . | . 5 1 \n" + \
                               " 8 1 3 | 4 5 6 | . . . \n" + \
                               " 2 5 7 | 1 . . | 4 3 6 \n" + \
                               " - - - + - - - + - - -\n" + \
                               " 9 6 4 | . 1 5 | 3 2 8 \n" + \
                               " 7 3 . | . 8 2 | 5 9 4 \n" + \
                               " . 2 . | 9 3 4 | 1 6 7 \n"
        current_board_string = self.test_generator.get_board_format_to_print(board_to_format)
        self.assertEquals(expected_board_print, current_board_string)

    def test_generate_sudoku_pattern_by_complexity_returns_solvable_sudoku_easy(self):
        self.test_generator.generate_sudoku_pattern_by_complexity(20, 25, '.')
        raw_sudoku_string = self.test_generator.get_board_format_to_string(self.test_generator.sudoku_pattern)
        sudoku_test_solve = BacktrakingAlgorithm(raw_sudoku_string, ".")
        self.assertTrue(sudoku_test_solve.solve_sudoku())

    def test_generate_sudoku_pattern_by_complexity_returns_solvable_sudoku_medium(self):
        self.test_generator.generate_sudoku_pattern_by_complexity(30, 40, '.')
        raw_sudoku_string = self.test_generator.get_board_format_to_string(self.test_generator.sudoku_pattern)
        sudoku_test_solve = BacktrakingAlgorithm(raw_sudoku_string, ".")
        self.assertTrue(sudoku_test_solve.solve_sudoku())

    def test_generate_sudoku_pattern_by_complexity_returns_solvable_sudoku_hard(self):
        self.test_generator.generate_sudoku_pattern_by_complexity(40, 50, '.')
        raw_sudoku_string = self.test_generator.get_board_format_to_string(self.test_generator.sudoku_pattern)
        sudoku_test_solve = BacktrakingAlgorithm(raw_sudoku_string, ".")
        self.assertTrue(sudoku_test_solve.solve_sudoku())

    def test_give_hint_at_returns_the_value_6_at_position_3_2(self):
        self.test_generator.board_list =[[6, 5, 7, 1, 8, 4, 3, 2, 9],
                                         [9, 2, 8, 7, 3, 6, 4, 1, 5],
                                         [4, 3, 1, 2, 9, 5, 7, 6, 8],
                                         [2, 8, 6, 3, 5, 9, 1, 4, 7],
                                         [7, 9, 5, 4, 2, 1, 8, 3, 6],
                                         [3, 1, 4, 8, 6, 7, 5, 9, 2],
                                         [8, 7, 9, 6, 1, 3, 2, 5, 4],
                                         [1, 6, 2, 5, 4, 8, 9, 7, 3],
                                         [5, 4, 3, 9, 7, 2, 6, 8, 1]]
        self.test_generator.sudoku_pattern = [['6', '.', '7', '.', '8', '4', '3', '2', '9'],
                                              ['.', '2', '8', '7', '3', '.', '4', '1', '5'],
                                              ['4', '3', '1', '2', '.', '.', '.', '6', '8'],
                                              ['2', '8', '.', '.', '5', '9', '1', '4', '7'],
                                              ['7', '9', '5', '4', '2', '.', '8', '3', '.'],
                                              ['3', '1', '4', '8', '6', '.', '5', '9', '2'],
                                              ['8', '.', '9', '.', '1', '3', '2', '5', '4'],
                                              ['1', '6', '2', '5', '.', '8', '9', '7', '3'],
                                              ['.', '.', '3', '9', '7', '2', '6', '8', '1']]

        expected_value_hint = 6
        self.assertEquals(expected_value_hint,self.test_generator.give_hint_at(3,2))