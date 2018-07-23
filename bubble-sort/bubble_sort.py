import unittest

def bubble_sort(lst):
    # set range for comparison: n, n-1, n-2...etc
    for num in range(len(lst)-1, 0, -1):
        # compare within set range
        for idx in range(num): 
            # compare element with right neighbor
            if lst[idx] > lst[idx + 1]:
                # swap if greater than
                # copy largest value to temp
                temp = lst[idx]
                # swap values (smaller goes to index of larger elem)
                lst[idx] = lst[idx + 1]
                # reassign temp to index + 1 (larger value)
                lst[idx + 1] = temp
    return lst


class Test(unittest.TestCase):

    def test_list_is_empty(self):
        actual = bubble_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test__list_has_one_element(self):
        actual = bubble_sort([2])
        expected = [2]
        self.assertEqual(actual, expected)

    def test_list_has_two_elements(self):
        actual = bubble_sort([2, 1])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_list_has_negative_nums(self):
        actual = bubble_sort([2, 1, 100, -22, 8, -1, 17])
        expected = [-22, -1, 1, 2, 8, 17, 100]
        self.assertEqual(actual, expected)

    def test_list_has_postive_nums(self):
        actual = bubble_sort([2, 1, 100, 22, 8, 17])
        expected = [1, 2, 8, 17, 22, 100]
        self.assertEqual(actual, expected)



unittest.main(verbosity=2)