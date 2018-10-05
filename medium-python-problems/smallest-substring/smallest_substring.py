import unittest

def smallest_substring(string, alphabet):
    '''Write a function that takes an input string and an alphabet, and returns the shortest substring of the input which contains every letter of the alphabet at least once.

        Input: "aaccbc"

        Alphabet: 'abc'

        Output: "accb" '''

    # fail fast if alphabet longer than string (no test)
    if len(alphabet) > len(string):
        raise ValueError('Alphabet is longer than the string')

    results = set()
    for substring in range(3, len(string) + 1):
        for index in range(len(string)+ 1 - substring):
            results.add(string[index:index + substring])

    smallest = sorted(results, key=len)[-1]

    for item in results:
        if len(item) < len(smallest) and all((char in item) for char in alphabet):
            smallest = item
    return smallest


class Test(unittest.TestCase):

    def test_smallest_substring_1(self):
        actual = smallest_substring('aaccbc', 'abc')
        expected = 'accb'
        self.assertEqual(actual, expected)

    def test_smallest_substring_2(self):
        actual = smallest_substring('aacbbbc', 'abc')
        expected = 'acb'
        self.assertEqual(actual, expected)

    def test_smallest_substring_3(self):
        actual = smallest_substring('aaaaabbbbbbbbccccccd', 'abcd')
        expected = 'abbbbbbbbccccccd'
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
