"""
Author: Maria Ledezma
Creation Date: 07/11/2013
"""
import unittest 
import sys 
sys.path.append( '../libs' ) 
from bit_handler import BitHandler

class TestBitHandler(unittest.TestCase): 

    def test_bit_count_of_0x1ff_returns_9(self):
        bits = 0x1ff
        expected_count_of_bits = 9
        current_count_of_bits = BitHandler.bit_count(bits)
        self.assertEquals(expected_count_of_bits,current_count_of_bits)

    def test_bit_count_of_0xaa_returns_4(self):
        bits = 0xaa
        expected_count_of_bits = 4
        current_count_of_bits = BitHandler.bit_count(bits)
        self.assertEquals(expected_count_of_bits,current_count_of_bits)

    def test_bit_for_of_9_returns_256(self):
        number = 9
        expected_bitfield = 2**(number-1)
        current_bitfield = BitHandler.bit_for(number)
        self.assertEquals(expected_bitfield,current_bitfield)

    def test_bit_for_of_1_returns_1(self):
        number = 1
        expected_bitfield = 2**(number-1)
        current_bitfield = BitHandler.bit_for(number) 
        self.assertEquals(expected_bitfield,current_bitfield)

    def test_bit_list_of_0x1ff_generates_list_of_numbers_between_1_to_9(self):
        bits = 0x1ff
        expected_list_number =[1, 2, 3, 4, 5, 6, 7, 8, 9]
        current_list_number = BitHandler.bit_list(bits)
        self.assertEquals(expected_list_number,current_list_number)

    def test_bit_list_of_0xaa_generates_list_of_even_numbers_between_2_to_8(self):
        bits = 0xaa
        expected_list_number =[2, 4, 6, 8]
        current_list_number = BitHandler.bit_list(bits)
        self.assertEquals(expected_list_number,current_list_number)