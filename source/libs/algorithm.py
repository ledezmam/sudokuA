import time

class Algorithm(object):
    
    def __init__(self, sudoku_to_solve, empty_spot_char):
        """Contructor of Algorithm.

        Keyword arguments:
        sudoku_to_solve -- the raw data of the sudoku to solve
        empty_spot_char -- the character which represents the places to be filled
        """
        
        # the start time when the sudoku starts being solve
        self.start_time = 0.0
        # the end tine when the sudoku was solved
        self.end_time = 0.0
        self.sudoku_to_solve = sudoku_to_solve
        #the character that is used as blank space
        self.empty_spot_char = empty_spot_char
        # the possible digits that the sudoku will contain
        self.digits   = '123456789'
        # the size of the sudoku to solve
        self.size_sudoku = 9

    def solve_sudoku(self):
        """Return the solution for the sudoku."""
        raise Exception("Implement the method")

    def generate_sudoku(self):
        """Generate a sudoku."""
        raise Exception("Implement the method")

    def sudoku_data_is_valid(self): 
        """Verifies if the sudoku to solve contains the valid data
            Return True if is valid False if a contradiction is found.
            
        """
        result = True
        list_chars = [char for char in self.sudoku_to_solve if char in self.digits\
                 or char in self.empty_spot_char]
        # verifies if the sudoku contains the correct number of characters
        if len(list_chars) != (self.size_sudoku ** 2):
            result = False
                    
        return result

    def get_time(self):
        """Returns the time that takes to solve the sudoku."""
        return self.end_time - self.start_time
        
    def get_sudoku_to_solve(self):
        """Returns the sudoku to solve."""
        return self.sudoku_to_solve

    def set_sudoku_to_solve(self, new_sudoku_to_solve):
        """Set a new soduku to solve.

        Keyword arguments:
        new_sudoku_to_solve -- the new sudoku to solve

        """
        self.sudoku_to_solve = new_sudoku_to_solve
        #Set to initial values the times values
        self.start_time = 0.0   
        self.end_time = 0.0        

    
