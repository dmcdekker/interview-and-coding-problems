import unittest

def search_index_position(arr, target):
    length = len(arr)
    if target > arr[length-1]:
            return length
    for idx, num in enumerate(arr):
        if num >= target:
            return idx

class Test(unittest.TestCase):

    def test_search_index_pos_1(self):
        actual = search_index_position([1,4,7,8], 2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_search_index_pos_2(self):
        actual = search_index_position([1,3,5,6], 4)
        expected = 2
        self.assertEqual(actual, expected)

    def test_search_index_pos_3(self):
        actual = search_index_position([1,3,5,6], 7)
        expected = 4
        self.assertEqual(actual, expected)  

unittest.main(verbosity=2)

