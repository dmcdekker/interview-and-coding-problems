import unittest

def quick_sort(lst):
    less = []
    equal = []
    greater = []
    if len(lst) > 1:
        pivot = lst[0]
        for num in lst:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        return quick_sort(less) + equal + quick_sort(greater)  
    else:  
        return lst


def quick_sort(lst):
      if len(lst) < 2:
          return lst
      else:
          pivot = lst[0]
          less = [num for num in lst[num:] if num <= pivot]
          greater = [num for num in lst[num:] if num > pivot]
          return quick_sort(less) + [pivot] + quick_sort(greater)


class Test(unittest.TestCase):

    def test_list_is_empty(self):
        actual = quick_sort([])
        expected = []
        self.assertEqual(actual, expected)

    def test__list_has_one_element(self):
        actual = quick_sort([2])
        expected = [2]
        self.assertEqual(actual, expected)

    def test_list_has_two_elements(self):
        actual = quick_sort([2, 1])
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_list_has_negative_nums(self):
        actual = quick_sort([2, 1, 100, -22, 8, -1, 17])
        expected = [-22, -1, 1, 2, 8, 17, 100]
        self.assertEqual(actual, expected)

    def test_list_has_postive_nums(self):
        actual = quick_sort([2, 1, 100, 22, 8, 17])
        expected = [1, 2, 8, 17, 22, 100]
        self.assertEqual(actual, expected)



unittest.main(verbosity=2)