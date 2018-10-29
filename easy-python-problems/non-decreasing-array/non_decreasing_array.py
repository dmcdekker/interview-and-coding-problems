import unittest

def non_decreasing_array(nums):
    '''Return true if array is one number away from being a decreasing array'''
    result = 0
    for idx in range(len(nums) -1):
        # if inversion is found
        if nums[idx] > nums[idx + 1]:
            # fix current and following value to check that inversion is detected properly
            if idx != 0 and nums[idx - 1] > nums[idx + 1]:
                nums[idx + 1] = nums[idx]
            result += 1
    return result <= 1 

class Test(unittest.TestCase):

    def test_non_decreasing_array_1(self):
        actual = non_decreasing_array([4, 2, 3])
        expected = True
        self.assertEqual(actual, expected)

    def test_non_decreasing_array_2(self):
        actual = non_decreasing_array([4, 5, 3])
        expected = True
        self.assertEqual(actual, expected)

    def test_non_decreasing_array_3(self):
        actual = non_decreasing_array([4, 2, 1])
        expected = False
        self.assertEqual(actual, expected)

    def test_non_decreasing_array_4(self):
        actual = non_decreasing_array([3, 4, 2, 3])
        expected = False
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
