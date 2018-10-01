import unittest

def rotLeft(a, d):
    '''Rotate an array to the left'''
    return a[d:] + a[:d]



class Test(unittest.TestCase):

    def test_rotate_4(self):
        actual = rotLeft([1, 2, 3, 4, 5], 4)
        expected = [5, 1, 2, 3, 4]
        self.assertEqual(actual, expected)

    def test_rotate_2(self):
        actual = rotLeft([1, 2, 3, 4, 5], 2)
        expected = [3, 4, 5, 1, 2]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)