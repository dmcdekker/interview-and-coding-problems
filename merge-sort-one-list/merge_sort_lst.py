import unittest

def merge(lst1, lst2):
    '''Function to merge two arrays'''
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

def mergesort(alist):
    '''Function to sort an array using merge sort algorithm'''
    if len(alist) == 0 or len(alist) == 1:
        return alist
    else:
        middle = len(alist)// 2
        lst1 = mergesort(alist[:middle])
        lst2 = mergesort(alist[middle:])
        return merge(lst1, lst2)


print mergesort([4, 2, 6, 1, 15, -3])

class Test(unittest.TestCase):

    def test_list_is_empty(self):
        actual = mergesort([])
        expected = []
        self.assertEqual(actual, expected)

    def test__list_has_one_element(self):
        actual = mergesort([2])
        expected = [2]
        self.assertEqual(actual, expected)

    def test_list_has_two_elements(self):
        actual = mergesort([2, 1])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_list_has_negative_nums(self):
        actual = mergesort([2, 1, 100, -22, 8, -1, 17])
        expected = [-22, -1, 1, 2, 8, 17, 100]
        self.assertEqual(actual, expected)

    def test_list_has_postive_nums(self):
        actual = mergesort([2, 1, 100, 22, 8, 17])
        expected = [1, 2, 8, 17, 22, 100]
        self.assertEqual(actual, expected)



unittest.main(verbosity=2)