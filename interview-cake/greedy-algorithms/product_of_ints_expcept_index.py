import unittest
import operator
from functools import reduce


def get_products_of_all_ints_except_at_index(int_list):
    '''Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products'''
    
    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')
    
    # Interview Cake Solution
    # product_results = [None] * len(int_list)
    
    # add products before current index to list
    # product_so_far = 1
    # for i in range(len(int_list)):
    #     product_results[i] = product_so_far
    #     product_so_far *= int_list[i]
    
    # product_so_far = 1
    # for i in range(len(int_list) - 1, -1, -1):
    #     product_results[i] *= product_so_far
    #     product_so_far *= int_list[i]
    
    size = len(int_list)
    
    # output array 
    output = [1] * size

    # left side: 0 - idx
    # left = 1
    for num in range(size - 1):
        left = reduce(lambda x,y: x*y, int_list[:num+1])
        output[num + 1] *= left

    # right side: idx - end
    # right = 1
    for num in range(size - 1, 0, -1):
        right = reduce(lambda x,y: x*y, int_list[num:])
        output[num - 1] *= right
    return output


# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)