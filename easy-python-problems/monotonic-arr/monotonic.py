import unittest

def is_monotonic(A):
    """
    :type A: List[int]
    :rtype: bool
    """
    sorted_a = sorted(A)
    sorted_reversed = list(reversed(sorted_a))
    if A == sorted_a or A == sorted_reversed:
        return True
    return False

class Test(unittest.TestCase):

    def test_is_monotonic_1(self):
        actual = is_monotonic([6,5,4,4])
        expected = True
        self.assertEqual(actual, expected)

    def test_is_monotonic_2(self):
        actual = is_monotonic([1,3,2])
        expected = False
        self.assertEqual(actual, expected)

    def test_is_monotonic_3(self):
        actual = is_monotonic([1,2,3])
        expected = True
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)


