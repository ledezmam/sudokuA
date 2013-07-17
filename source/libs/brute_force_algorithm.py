import sys 
import time
from algorithm import Algorithm 
from bit_handler import BitHandler 

class BruteForceAlgorithm(Algorithm):

    def __init__(self, sudoku_to_solve, empty_spot_char):
        """Make a blank puzzle

            Keyword arguments:
            sudoku_to_solve -- the raw data a multi-line string 9 chars x 9 lines with the game to solve
            empty_spot_char -- the character which represents the places to be filled

        """

        """rows[i] stores the set of possible values that an unset cell in
           row i could take. Similarly for cols and blocks.
           cells stores the cells which have been set so far. If they are
           unset, the value is None, otherwise it is a number from 0 to 9.

        """

        super(BruteForceAlgorithm, self).__init__(sudoku_to_solve, empty_spot_char)
        init_value_hexadecimal = 0x1ff
        self.rows = [ init_value_hexadecimal for i in range(9) ]
        self.cols = [ init_value_hexadecimal for i in range(9) ]
        self.blocks = [[ init_value_hexadecimal for i in range(3)] for j in range(3)]
        self.cells = [[ None for i in range(9)] for j in range(9)]

    def get_candidates(self, row, col):
        """Return the possible values which this cell could have

            Keyword arguments:
            row -- the index of the row of the value to be evaluated e.g. 1
            col -- the index of the column of the value to be evaluated e.g. 6

        """

        assert(self.cells[row][col] == None)
        return self.rows[row] & self.cols[col] & self.blocks[row / 3][col / 3]

    def set_cell(self, row, col, num):
        """Fill in the cell at (row, col) with value num

            Keyword arguments:
            row -- the index of the row to place the new value
            col -- the index of the column to place the new value
            num -- the new value to set in the cell at (row, col)

        """

        bit = BitHandler.bit_for(num)
        # Make sure that the bit is acceptable
        assert self.cells[row][col] == None
        assert self.get_candidates(row, col) & bit != 0

        # No cell in this row, column or block can now have this value
        self.rows[row] &= ~bit
        self.cols[col] &= ~bit
        self.blocks[row / 3][col / 3] &= ~bit

        # and set it
        self.cells[row][col] = num

    def unset_cell(self, row, col, num):
        """Erase the cell at (row, col), updating rows, cols and blocks.
           
            Keyword arguments:
            row -- the index of the row to erase the value
            col -- the index of the column to erase the value
            num -- the value to erase if it is placed at (row, col)

        """

        bit = BitHandler.bit_for(num)

        # Make sure it was already set        
        assert self.cells[row][col] == num
        assert self.rows[row] & self.cols[col] & self.blocks[row / 3][col / 3] & bit == 0

        self.rows[row] |= bit
        self.cols[col] |= bit
        self.blocks[row / 3][col / 3] |= bit
        self.cells[row][col] = None

    def find_minimum(self, evaluate_index):
        """Pick the cell with the smallest number of candidates
           that satisfies evaluate_index(i, j).  Returns None if no unset cells
           satisfy evaluate_index.

           Keyword arguments:
            evaluate_index -- the anonimous function that evaluates index i, j (row, column) and returns boolean e.g. True

        """
        minimum = None
        minimum_position = None
        for i in range(9):
            for j in range(9):
                if self.cells[i][j] == None:
                    if evaluate_index(i, j) and (minimum == None or BitHandler.bit_count(self.get_candidates(i, j)) < minimum):
                        minimum = BitHandler.bit_count(self.get_candidates(i, j))
                        minimum_position = (i, j)

        return minimum_position

    def execute_algorithm(self, evaluate_index, destructive, check_blocks):
        """Executes the algorithm that solves the sudoku
            Tries to solve the puzzle in-place, filling only those cells
            which satisfy evaluate_index. If destructive is false it will undo all of
            its changes once it is finished.
            If check_blocks is true it will try to fill in each 3x3 block
            separately before it starts - if it can't do that then it can't
            solve the puzzle

            Keyword arguments:
            evaluate_index -- the anonimous function that evaluates index i, j (row, column) and returns boolean e.g. True
            destructive -- boolean value that determines to erase a value or not
            check_blocks -- boolean value that determines if a cell can be filled
            
        """
        # First of all, check that each block can be filled in some way
        if check_blocks is True:
            for i in range(3):
                for j in range(3):
                    if not self.execute_algorithm(lambda i2, j2: i2 / 3 == i and j2 / 3 == j, False, False):
                        return False

        # Now solve the puzzle by brute force

        minimum = self.find_minimum(evaluate_index)

        if minimum is None:
            return True

        # We'll brute force on this cell
        (i, j) = minimum

        for num in BitHandler.bit_list(self.get_candidates(i, j)):
            # Try num on cell (i, j)
            self.set_cell(i, j, num)

            if self.execute_algorithm(evaluate_index, destructive, check_blocks):
                if not destructive:
                    self.unset_cell(i, j, num)
                return True

            self.unset_cell(i, j, num)

        # We've exhausted all possibilities so the puzzle is unsolvable
        return False

    def solve_sudoku(self):
        """Verifies the candidates per position i,j and calls to the algorithm for resolving the sudoku.
            Returns the sudoku solved if it was resolvable otherwise returns a empty list

        """
        solved_sudoku = []
        if self.sudoku_data_is_valid() is True:            
            self.start_time = time.clock()  
            list_lines = self.sudoku_to_solve.split('\n')
            for i in range(9):
                line = list_lines[i].strip()
                for j in range(9):
                    current_character = line[j]
                    if ord(current_character) >= ord('1') and ord(current_character) <= ord('9'):
                        if self.get_candidates(i, j) & BitHandler.bit_for(int(current_character)) == 0:
                            sys.exit(0)
                        else:
                            self.set_cell(i, j, int(current_character))
                    elif current_character == self.empty_spot_char:
                        pass
                    else:
                        raise Exception, "Bad input: " + current_character
            if self.execute_algorithm(lambda i, j: True, True, True):
                self.convert_matrix_solved_in_str_matrix()
                self.end_time = time.clock()
                solved_sudoku = self.cells
        return solved_sudoku

    def convert_matrix_solved_in_str_matrix(self):
        """Converts the int matrix to char matrix to follow the format of other algorithms"""
        for i in range(9):
            for j in range (9):
                self.cells[i][j] = str(self.cells[i][j])