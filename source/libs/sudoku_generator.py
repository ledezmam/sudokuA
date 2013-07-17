import random
import copy

class SudokuGenerator:
    
    def __init__(self):
        """Constructor that initiates the board of sudoku as an empty list"""
        self.board_list = []
        self.sudoku_pattern = []

    def generate(self):
        """Calls fill_board method to generate sudoku board with the list of positions (column, row)
             of the board_list and initial index 

        """
        index = 0
        positions = self.get_positions()
        self.fill_board(positions, index)

    def initiate_board_with_zeros(self, number_to_fill = 9):
        """Fill in the board_list with zeros"""
        row = [0 * i for i in range(number_to_fill)]
        for i in range(0, 9):
            self.board_list.append(row[:])

    def get_positions(self):
        """ Gets the list of postions/coordinates of the whole board, returns a list of tuples
            (column, row)
        """
        positions = []
        self.initiate_board_with_zeros()

        for j in range(0, 9):
            for i in range(0, 9):
                positions.append((i, j))
        return positions

    def generate_numbers_to_fill_order(self):
        """Generates numbers 1 - 9 to be used as values of sudoku cells"""
        generated_numbers = []
        for i in range(1, 10):
            generated_numbers.append(i)
        return generated_numbers

    def get_fill_order_list(self):
        """Gets a list of random numbers that will be used to collect the coordinates 
            from positions.

        """
        random.seed()
        generated_numbers = self.generate_numbers_to_fill_order()
        fill_order = []
        while len(generated_numbers) > 0:
            i = random.randint(0, len(generated_numbers)-1)
            fill_order.append(generated_numbers[i])
            del generated_numbers[i]
        return fill_order


    def fill_board(self, positions, index):
        """Recursive method that searches the locations for the numbers of sudoku
            and fills the board_list with the numbers for sudoku
            If sudoku can be generated will return True otherwise False

            Keyword arguments:
            positions -- the list of coordinates (col, row) e.g. [(0, 0), (1, 0), etc]
            index -- the index of each cell (0 - 81) e.g. 51

        """
        fill_order = self.get_fill_order_list()
        
        if len(positions) == index:
            return self.is_valid_board()

        for i in fill_order:
            x = positions[index][0]
            y = positions[index][1]
            self.board_list[x][y] = i
            
            if self.is_valid_board() is True:
                if self.fill_board(positions, index + 1) is True:
                    return True
            self.board_list[x][y] = 0
        return False

    def is_valid_board(self):
        """Verifies that there are not duplicated values in rows, columns and in each square,
            return True if there are not duplicated values

        """
        result = True
        for i in range(0, 9):
            if (not self.is_valid_row(i)) or (not self.is_valid_col(i)) or \
                                                     (not self.is_valid_square(i)):
                result = False
        return result

    def is_valid_col(self, col):
        """Returns True if it's a valid column without duplicates
            
            Keyword arguments:
            col -- the index of the column (0 - 8) to be evaluated e.g. 4

        """
        result = True
        found_list = []
        for i in range(0, 9):
            if not self.board_list[i][col] == 0:
                if self.board_list[i][col] in found_list:
                    result = False
                found_list.append(self.board_list[i][col])
        return result

    def is_valid_row(self, row):
        """Returns True if it's a valid row without duplicates

            Keyword arguments:
            row -- the index of the row (0 - 8) to be evaluated e.g. 4

        """
        result = True
        found_list = []
        for j in range(0, 9):
            if not self.board_list[row][j] == 0:
                if self.board_list[row][j] in found_list:
                    result = False
                found_list.append(self.board_list[row][j])        
        return result

    def is_valid_square(self, square):
        """Returns True if there are not duplicated values in the square. A square
            is each small quadrant (3 x 3)

            Keyword arguments:
            square -- the index of the quadrant to be evaluated e.g. 4
        """
        result = True
        found_list = []
        x_offset = (3 * (square % 3))
        y_offset = int(square / 3) * 3
        for j in range(0, 3):
            for i in range(0, 3):
                if not self.board_list[x_offset + i][y_offset + j] == 0:
                    if self.board_list[x_offset + i][y_offset + j] in found_list:                        
                        result = False
                    found_list.append(self.board_list[x_offset + i][y_offset + j])
        return result

    def generate_sudoku_pattern_by_complexity(self, min_holes, max_holes, empty_spot_char):
        """Saves in the sudoku_pattern, the pattern for the sudoku game with the 
            empty spot char defined; the complexity is defined by the number of holes
            to be used in the pattern.

            Keyword arguments:
            min_holes -- the number of minimum holes to set in the pattern e.g. 20
            max_holes --  the number of max_holes to set in the pattern e.g. 25
            empty_spot_char --  the character to be used as empty spot in the pattern e.g. '0'

        """
        self.generate()
        self.sudoku_pattern = copy.deepcopy(self.board_list)

        qty_holes = random.randint(min_holes, max_holes)
        list_positions = self.generate_random_positions(qty_holes)

        for i in range(9):
            for j in range(9):
                if (i, j) in list_positions:
                    self.sudoku_pattern[i][j] = empty_spot_char
                else:
                    self.sudoku_pattern[i][j] = str(self.sudoku_pattern[i][j])
   
    def generate_random_positions(self, size_positions):
        """Generates a list of random positions to place the empty spot char 

            Keyword arguments:
            size_positions -- the quantity of random positions to be generated e.g. 23
            
        """
        list_positions = []
        control_size = 0
        while control_size < size_positions:
            position = random.randint(0, 8), random.randint(0, 8)
            if position not in list_positions:
                list_positions.append(position)
                control_size += 1
        return list_positions

    def get_board_format_to_string(self, board):
        """Returns a string formatted for the input value for an algorithm solver

            Keyword arguments:
            board -- the list of lists to be formatted as string

        """
        size_board = len(board)
        string_format = ""

        for i in range(0, size_board):
            for j in range(0, size_board):
                string_format += str(board[i][j])
            string_format += "\n"
        return string_format

    def give_hint_at(self, row, col):
        """Returns the value at the row and column specified from the sudoku generated
            with all the values (board_list)
        
            Keyword arguments:
            row -- the index of the row for the postion to get the value
            col -- the index of the column for the postion to get the value

        """
        return self.board_list[row][col]