import unittest


def reverse(list_of_chars):
    '''Write a function that takes a list of characters 
       and reverses the letters in place'''

    # Reverse the input list of chars in place
    left_idx = 0
    right_idx = len(list_of_chars) - 1
    while left_idx < right_idx:
        list_of_chars[left_idx], list_of_chars[right_idx] = list_of_chars[right_idx], list_of_chars[left_idx] 
        left_idx += 1
        right_idx -= 1
        
# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)