import unittest

def remove_dupes(nums):
    '''Remove dupes from list in place'''
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del nums[i]
        else:
            i += 1
    return len(nums)

class Test(unittest.TestCase):

    def test_remove_dupes_1(self):
        actual = remove_dupes([0,0,1,1,1,2,2,3,3,4])
        expected = 5
        self.assertEqual(actual, expected)

    def test_remove_dupes_2(self):
        actual = remove_dupes([1,1,2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_remove_dupes_3(self):
        actual = remove_dupes([])
        expected = 0
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
