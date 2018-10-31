import unittest

def array_pair_sum(nums):
        '''Return min sum of pair in list'''
        new_nums = sorted(nums)  
        result = 0
        for i in range(0, len(new_nums)-1, 2):
            result += new_nums[i]
            if i == 2:
                break
        return result


class Test(unittest.TestCase):

    def test_array_pair_sum_1(self):
        actual = array_pair_sum([2, 4, 1, 3, 6, 5])
        expected = 4
        self.assertEqual = (actual, expected)

    def test_array_pair_sum_2(self):
        actual = array_pair_sum([10, 12, 6, 2, 15, 40])
        expected = 12
        self.assertEqual = (actual, expected)

    def test_array_pair_sum_3(self):
        actual = array_pair_sum([20, 30, 16, 12, 22, 32])
        expected = 32
        self.assertEqual = (actual, expected)


unittest.main(verbosity=2)