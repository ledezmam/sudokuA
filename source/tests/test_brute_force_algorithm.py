"""
Author: Maria Ledezma
Creation Date: 07/09/2013
"""
import unittest 
import sys 
sys.path.append( '../libs' ) 
from brute_force_algorithm import BruteForceAlgorithm 

class TestBruteForceAlgorithm(unittest.TestCase): 

    def test_verify_solution_easy_sudoku_empty_values_with_zero(self):
        raw_sudoku  = ("000000680\n" + \
                       "000073009\n" + \
                       "309000045\n" + \
                       "490000000\n" + \
                       "803050902\n" + \
                       "000000036\n" + \
                       "960000308\n" + \
                       "700680000\n" + \
                       "028000000")
        sudoku_test_solve = BruteForceAlgorithm(raw_sudoku, "0")
        square_result = [['1', '7', '2', '5', '4', '9', '6', '8', '3'],
                         ['6', '4', '5', '8', '7', '3', '2', '1', '9'],
                         ['3', '8', '9', '2', '6', '1', '7', '4', '5'],
                         ['4', '9', '6', '3', '2', '7', '8', '5', '1'],
                         ['8', '1', '3', '4', '5', '6', '9', '7', '2'],
                         ['2', '5', '7', '1', '9', '8', '4', '3', '6'],
                         ['9', '6', '4', '7', '1', '5', '3', '2', '8'],
                         ['7', '3', '1', '6', '8', '2', '5', '9', '4'],
                         ['5', '2', '8', '9', '3', '4', '1', '6', '7']]

        self.assertEquals(square_result, sudoku_test_solve.solve_sudoku())
    def test_verify_solution_easy_sudoku_empty_values_with_dot(self):
        raw_sudoku  = ("3.65.84..\n" + \
                       "52.......\n" + \
                       ".87....31\n" + \
                       "..3.1..8.\n" + \
                       "9..863..5\n" + \
                       ".5..9.6..\n" + \
                       "13....25.\n" + \
                       ".......74\n" + \
                       "..52.63..")
        sudoku_test_solve = BruteForceAlgorithm(raw_sudoku, ".")
        square_result = [['3', '1', '6', '5', '7', '8', '4', '9', '2'],
                         ['5', '2', '9', '1', '3', '4', '7', '6', '8'],
                         ['4', '8', '7', '6', '2', '9', '5', '3', '1'],
                         ['2', '6', '3', '4', '1', '5', '9', '8', '7'],
                         ['9', '7', '4', '8', '6', '3', '1', '2', '5'],
                         ['8', '5', '1', '7', '9', '2', '6', '4', '3'],
                         ['1', '3', '8', '9', '4', '7', '2', '5', '6'],
                         ['6', '9', '2', '3', '5', '1', '8', '7', '4'],
                         ['7', '4', '5', '2', '8', '6', '3', '1', '9']];
          
        self.assertEquals(square_result, sudoku_test_solve.solve_sudoku()) 
               
    def test_soduku_to_solve_only_contains_numbers(self):
        sudoku_test_only_numbers  = BruteForceAlgorithm("092300000\n" + \
                                                        "000080100\n" + \
                                                        "000000000\n" + \
                                                        "107040000\n" + \
                                                        "000000065\n" + \
                                                        "800000000\n" + \
                                                        "060502000\n" + \
                                                        "400000700\n" + \
                                                        "000900000", "0")
                
        self.assertTrue(sudoku_test_only_numbers.sudoku_data_is_valid())

    def test_soduku_to_solve_cannot_contain_letters(self):
        sudoku_test_only_numbers  = BruteForceAlgorithm("092300000\n" + \
                                                        "000080100\n" + \
                                                        "000000000\n" + \
                                                        "107040000\n" + \
                                                        "000000A65\n" + \
                                                        "800000000\n" + \
                                                        "060502000\n" + \
                                                        "400000C00\n" + \
                                                        "000900000", "0")
                
        self.assertFalse(sudoku_test_only_numbers.sudoku_data_is_valid())

    def test_soduku_to_solve_cannot_contain_dot_as_empty_value_if_the_empty_value_is_zero(self):
        sudoku_test_only_numbers  = BruteForceAlgorithm("092300000\n" + \
                                                        "....80100\n" + \
                                                        "...000000\n" + \
                                                        "107040000\n" + \
                                                        "..0..0465\n" + \
                                                        "800000000\n" + \
                                                        "060502000\n" + \
                                                        "400000200\n" + \
                                                        "000900000", "0")
                
        self.assertFalse(sudoku_test_only_numbers.sudoku_data_is_valid())

    def test_soduku_to_solve_not_contain_spaces_as_empty_value_if_the_empty_value_is_zero(self):
        sudoku_test_only_numbers  = BruteForceAlgorithm(" 923     \n" + \
                                                        "    8 1  \n" + \
                                                        "      1  \n" + \
                                                        "1 7 4    \n" + \
                                                        "      465\n" + \
                                                        "8        \n" + \
                                                        " 6 5 2   \n" + \
                                                        "4     2  \n" + \
                                                        "   9     ", "0")
                
        self.assertFalse(sudoku_test_only_numbers.sudoku_data_is_valid())

    def test_soduku_to_solve_is_valid_when_contains_81_numbers(self):
        sudoku_test_only_numbers  = BruteForceAlgorithm("092300000\n" + \
                                                        "000080100\n" + \
                                                        "000000000\n" + \
                                                        "107040000\n" + \
                                                        "000000065\n" + \
                                                        "800000000\n" + \
                                                        "060502000\n" + \
                                                        "400000700\n" + \
                                                        "000900000", "0")
                
        self.assertTrue(sudoku_test_only_numbers.sudoku_data_is_valid())


    def test_soduku_to_solve_is_invalid_when_contains_less_than_81_numbers(self):
        sudoku_test_only_numbers  = BruteForceAlgorithm("092300000\n" + \
                                                        "000080100\n" + \
                                                        "000000000\n" + \
                                                        "107040000\n" + \
                                                        "000000065\n" + \
                                                        "800000000\n" + \
                                                        "060502000", "0")
                
        self.assertFalse(sudoku_test_only_numbers.sudoku_data_is_valid())

    def test_soduku_to_solve_is_invalid_when_contains_more_than_81_numbers(self):
        sudoku_test_only_numbers  = BruteForceAlgorithm("092300000\n" + \
                                                        "000080100\n" + \
                                                        "000000000\n" + \
                                                        "107040000\n" + \
                                                        "000000065\n" + \
                                                        "800000000\n" + \
                                                        "060502000\n" + \
                                                        "400000700\n" + \
                                                        "000900000\n" + \
                                                        "000000065\n" + \
                                                        "060502000", "0")

    def test_soduku_to_solve_is_valid_when_characters_to_replace_are_dot(self):
        sudoku_test_only_numbers  = BruteForceAlgorithm(".923.....\n" + \
                                                        "....8.1..\n" + \
                                                        ".........\n" + \
                                                        "1.7.4....\n" + \
                                                        ".......65\n" + \
                                                        "8........\n" + \
                                                        ".6.5.2...\n" + \
                                                        "4.....7..\n" + \
                                                        "...9.....", ".")

    def test_soduku_to_solve_is_valid_when_characters_to_replace_are_porcentage(self):
        sudoku_test_only_numbers  = BruteForceAlgorithm("%923%%%%%\n" + \
                                                        "%%%%8%1%%\n" + \
                                                        "%%%%%%%%%\n" + \
                                                        "1%7%4%%%%\n" + \
                                                        "%%%%%%%65\n" + \
                                                        "8%%%%%%%%\n" + \
                                                        "%6%5%2%%%\n" + \
                                                        "4%%%%%7%%\n" + \
                                                        "%%%9%%%%%", "%")
                
        self.assertTrue(sudoku_test_only_numbers.sudoku_data_is_valid())