import unittest

def array_pair_sum(nums):
        '''Return min sum of pair in list'''
        new_nums = sorted(nums)
        result = 0
        for i in range(0, len(new_nums)-1, 2):
            result += new_nums[i]
        return result

class Test(unittest.TestCase):

    def test_array_pair_sum_1(self):
        actual = array_pair_sum([2, 4, 1, 3])
        expected = 4
        self.assertEqual = (actual, expected)

    def test_array_pair_sum_2(self):
        actual = array_pair_sum([10, 12, 6, 2])
        expected = 12
        self.assertEqual = (actual, expected)


unittest.main(verbosity=2)