import unittest

def insertion_sort(alist):

    for index in range(1,len(alist)):
        # element to be compared
        current = alist[index]
        # comparing current element with the sorted portion and swapping
        while index > 0 and alist[index - 1] > current:
            alist[index] = alist[index - 1]
            index -= 1
            alist[index] = current

    return alist


class Test(unittest.TestCase):

    def test_list_is_empty(self):
        actual = insertion_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test__list_has_one_element(self):
        actual = insertion_sort([2])
        expected = [2]
        self.assertEqual(actual, expected)

    def test_list_has_two_elements(self):
        actual = insertion_sort([2, 1])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_list_has_negative_nums(self):
        actual = insertion_sort([2, 1, 100, -22, 8, -1, 17])
        expected = [-22, -1, 1, 2, 8, 17, 100]
        self.assertEqual(actual, expected)

    def test_list_has_postive_nums(self):
        actual = insertion_sort([2, 1, 100, 22, 8, 17])
        expected = [1, 2, 8, 17, 22, 100]
        self.assertEqual(actual, expected)



unittest.main(verbosity=2)