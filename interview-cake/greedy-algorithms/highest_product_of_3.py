import unittest


def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('Need at least 3 numbers')
    sorted_ints = sorted(list_of_ints)
    # if two negative nums at beginning: use those to multiply
    return max(sorted_ints[0] * sorted_ints[1] * sorted_ints[-1], sorted_ints[-3] * sorted_ints[-2] * sorted_ints[-1])

# Interview Cake Solution
# def highest_product_of_3(list_of_ints):
    # Calculate the highest product of three numbers
    # set min int
    # highest_product_of_3 = (list_of_ints[0] * list_of_ints[1] * list_of_ints[2])
    # highest_product_of_2 = (list_of_ints[0] * list_of_ints[1])
    # lowest_product_of_2 = (list_of_ints[0] * list_of_ints[1])
    # highest = max(list_of_ints[0], list_of_ints[1])
    # lowest = min(list_of_ints[0], list_of_ints[1])
    
    # # error message if less than 3 values
    # if len(list_of_ints) < 3:
    #     raise ValueError('Need at least 3 numbers')
    # # iterate through list of ints
    # for num in range(2, len(list_of_ints)):
    #     current_int = list_of_ints[num]
    #     # store largest value of int
    #     highest_product_of_3 = max(highest_product_of_3, 
    #                                     current_int * highest_product_of_2,
    #                                     current_int * lowest_product_of_2)
        
    #     highest_product_of_2 = max(highest_product_of_2,
    #                               current_int * highest,
    #                               current_int * lowest)
        
    #     lowest_product_of_2 = min(lowest_product_of_2,
    #                               current_int * highest,
    #                               current_int * lowest)
        
    #     highest = max(highest, current_int)
        
    #     lowest = min(lowest, current_int)
        
    # return highest_product_of_3

# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)