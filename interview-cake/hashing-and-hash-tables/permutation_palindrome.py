import unittest


def has_palindrome_permutation(the_string):
    '''Write an efficient function that checks whether any permutation ↴ 
       of an input string is a palindrome'''

    # Check if any permutation of the input is a palindrome
    is_palindrome = {}
    for letter in the_string:
        is_palindrome[letter] = is_palindrome.get(letter, 0) + 1
 
    count = 0
    for val in is_palindrome.values():
        if val % 2 != 0:
            count += 1
    return count <= 1      

# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)