import unittest


def merge_lists(lst1, lst2):
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1

    new_lst = []
    idx1 = 0
    idx2 = 0
    while idx1 < len(lst1) and idx2 < len(lst2):
        if lst1[idx1] <= lst2[idx2]:
            new_lst.append(lst1[idx1])
            idx1 += 1
        else:
            new_lst.append(lst2[idx2])
            idx2 += 1

    new_lst.extend(lst1[idx1:])
    new_lst.extend(lst2[idx2:])

    return new_lst


# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)