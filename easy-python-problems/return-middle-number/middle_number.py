import unittest

def peak_index(A):
        """
        Return the value at the peak index 
        """
        peak = 0
        for idx in range(1, len(A)-1):
            if A[idx] > A[idx-1]:
                peak = idx
        return peak

class Test(unittest.TestCase):

    def test_peak_index_1(self):
        actual = peak_index([1, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_peak_index_2(self):
        actual = peak_index([1, 2, 1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_peak_index_3(self):
        actual = peak_index([0, 10, 5, 2])
        expected = 1
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
