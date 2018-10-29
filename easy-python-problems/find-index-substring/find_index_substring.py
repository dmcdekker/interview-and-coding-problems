import unittest

def find_index_substring(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1

class Test(unittest.TestCase):

    def test_find_index_substring_1(self):
        actual = find_index_substring('hello', 'll')
        expected = 2
        self.assertEqual(actual, expected)

    def test_find_index_substring_2(self):
        actual = find_index_substring('working', 'in')
        expected = 4
        self.assertEqual(actual, expected)

    def test_find_index_substring_3(self):
        actual = find_index_substring('working', '')
        expected = 0
        self.assertEqual(actual, expected)

    def test_find_index_substring_4(self):
        actual = find_index_substring('working', 'zz')
        expected = -1
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
