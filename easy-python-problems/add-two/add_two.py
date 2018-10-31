import unittest
import collections
'''Return list of numbers that sum to the target number'''

def two_sum_v1(nums, target):
    # num_dict = {}
    # for idx, val in enumerate(nums):
    #     diff = target - val
    #     if diff in num_dict:
    #         return [num_dict[diff], idx]
    #     num_dict[val] = idx

    num_dict = {}
    for idx, val in enumerate(nums):
        num_dict[val] = idx

    for key, value in num_dict.items():
        diff = target - key
        if diff in num_dict:
            return [value, num_dict[diff]]
    return '{}'.format('No matches')



class Test(unittest.TestCase):

    def test_two_sum_1(self):
        actual = two_sum_v1([2, 7, 11, 13], 9)
        expected = [0, 1] 
        self.assertEqual(actual, expected)

    def test_two_sum_2(self):
        actual = two_sum_v1([2, 7, 11, -1], 10)
        expected = [2, 3]
        self.assertEqual(actual, expected)

    def test_two_sum_3(self):
        actual = two_sum_v1([5, -11, 15, 10], 20)
        expected = [0, 2]
        self.assertEqual(actual, expected)

    def test_two_sum_no_match(self):
        actual = two_sum_v1([2, 7, 11, -1], 20)
        expected = 'No matches'
        self.assertEqual(actual, expected)



unittest.main(verbosity=2)