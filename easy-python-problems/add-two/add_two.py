import unittest
  

def two_sum_v1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    num_dict = {}
    for idx, val in enumerate(nums):
        diff = target - val
        if diff in num_dict:
            return [num_dict[diff], idx]
        num_dict[val] = idx

class Test(unittest.TestCase):

    def test_two_sum_1(self):
        actual = two_sum_v1([2, 7, 11, 13], 9)
        expected = [0, 1] 
        self.assertEqual(actual, expected)

    def test_two_sum_2(self):
        actual = two_sum_v1([2, 7, 11, -1], 10)
        expected = [2, 3]
        self.assertEqual(actual, expected)






unittest.main(verbosity=2)