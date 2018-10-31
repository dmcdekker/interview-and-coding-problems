import unittest

def max_sub_array(nums):
    ''' Kadane's algorithm'''
    # # max_ending: look for all positive contiguous segments of the array
    # # max_current = maximum sum contiguous segment among all positive segments
    # max_ending = max_current = nums[0]
    # # use list slicing to traverse nums list
    # for sub_array in nums[1:]:
    #     max_ending = max(sub_array, max_ending + sub_array)
    #     max_current = max(max_current, max_ending)
    # return max_current

    # max_ending: look for all positive contiguous segments of the array
    # max_current = maximum sum contiguous segment among all positive segments

    max_so_far = nums[0]
    max_ending = nums[0]

    for idx in range(0, len(nums)-1): 
        # increment max_ending with next value
        max_ending += nums[idx] 
        # add to max_so_far if greater than
        if (max_so_far < max_ending): 
            # assign new value
            max_so_far = max_ending 
        # return largest value
        if max_ending < 0: 
            max_ending = 0   
    return max_so_far

class Test(unittest.TestCase):

    def test_max_sub_array_1(self):
        actual = max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        expected = 6
        self.assertEqual(actual, expected)

    def test_max_sub_array_2(self):
        actual = max_sub_array([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7])
        expected = -3
        self.assertEqual(actual, expected)



unittest.main(verbosity=2)



