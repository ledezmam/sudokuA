import unittest
import sys
sys.path.append( '../libs' )
from export_sudoku import ExportSudoku

class TestExportSudoku(unittest.TestCase):

    def test_the_format_to_export_is_correct(self):

        square = [['1', '7', '2', '5', '4', '9', '6', '8', '3'],
                  ['6', '4', '5', '8', '7', '3', '2', '1', '9'],
                  ['3', '8', '9', '2', '6', '1', '7', '4', '5'],
                  ['4', '9', '6', '3', '2', '7', '8', '5', '1'],
                  ['8', '1', '3', '4', '5', '6', '9', '7', '2'],
                  ['2', '5', '7', '1', '9', '8', '4', '3', '6'],
                  ['9', '6', '4', '7', '1', '5', '3', '2', '8'],
                  ['7', '3', '1', '6', '8', '2', '5', '9', '4'],
                  ['5', '2', '8', '9', '3', '4', '1', '6', '7']]

        expected = " 1 7 2 | 5 4 9 | 6 8 3 \n" + \
                   " 6 4 5 | 8 7 3 | 2 1 9 \n" + \
                   " 3 8 9 | 2 6 1 | 7 4 5 \n" + \
                   " - - - + - - - + - - -\n" + \
                   " 4 9 6 | 3 2 7 | 8 5 1 \n" + \
                   " 8 1 3 | 4 5 6 | 9 7 2 \n" + \
                   " 2 5 7 | 1 9 8 | 4 3 6 \n" + \
                   " - - - + - - - + - - -\n" + \
                   " 9 6 4 | 7 1 5 | 3 2 8 \n" + \
                   " 7 3 1 | 6 8 2 | 5 9 4 \n" + \
                   " 5 2 8 | 9 3 4 | 1 6 7 \n"
     
        export_sudoku = ExportSudoku()
        line_to_export = export_sudoku.get_format_sudoku(square)
        self.assertEquals(line_to_export, expected)

    def test_the_format_to_export_is_correct_empty_fields_dot(self):

        square = [['1', '.', '2', '5', '4', '9', '.', '.', '3'],
                  ['.', '.', '.', '8', '7', '3', '2', '1', '9'],
                  ['3', '8', '9', '.', '.', '.', '.', '.', '.'],
                  ['4', '9', '.', '.', '.', '.', '.', '.', '.'],
                  ['8', '1', '3', '4', '5', '6', '9', '7', '2'],
                  ['.', '.', '.', '.', '.', '.', '.', '3', '6'],
                  ['9', '6', '4', '.', '.', '.', '.', '2', '8'],
                  ['.', '.', '.', '.', '.', '.', '5', '.', '4'],
                  ['5', '2', '8', '.', '.', '.', '1', '6', '.']]

        expected = " 1 . 2 | 5 4 9 | . . 3 \n" + \
                   " . . . | 8 7 3 | 2 1 9 \n" + \
                   " 3 8 9 | . . . | . . . \n" + \
                   " - - - + - - - + - - -\n" + \
                   " 4 9 . | . . . | . . . \n" + \
                   " 8 1 3 | 4 5 6 | 9 7 2 \n" + \
                   " . . . | . . . | . 3 6 \n" + \
                   " - - - + - - - + - - -\n" + \
                   " 9 6 4 | . . . | . 2 8 \n" + \
                   " . . . | . . . | 5 . 4 \n" + \
                   " 5 2 8 | . . . | 1 6 . \n"
     
        export_sudoku = ExportSudoku()
        line_to_export = export_sudoku.get_format_sudoku(square)
        self.assertEquals(line_to_export, expected)

    def test_export_sudoku_returns_false_when_no_valid_export_type(self):
        square = [['1', '.', '2', '5', '4', '9', '.', '.', '3'],
                  ['.', '.', '.', '8', '7', '3', '2', '1', '9'],
                  ['3', '8', '9', '.', '.', '.', '.', '.', '.'],
                  ['4', '9', '.', '.', '.', '.', '.', '.', '.'],
                  ['8', '1', '3', '4', '5', '6', '9', '7', '2'],
                  ['.', '.', '.', '.', '.', '.', '.', '3', '6'],
                  ['9', '6', '4', '.', '.', '.', '.', '2', '8'],
                  ['.', '.', '.', '.', '.', '.', '5', '.', '4'],
                  ['5', '2', '8', '.', '.', '.', '1', '6', '.']]

        export_sudoku = ExportSudoku()
        line_to_export = export_sudoku.export_sudoku(square, "Outlook", "", "")
        self.assertFalse(line_to_export)

if __name__ == "__main__":
    unittest.main()
