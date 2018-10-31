import unittest
  
'''Return true if the sum of any two elements equal the target number'''

def two_sum_v1(nums, target):
    num_dict = {}
    for idx, num in enumerate(nums):  
        diff = target - num
        # if the difference has already been recorded return it   
        if diff in num_dict:
            return [num_dict[diff], idx]
        # or add to the dictionary
        else:
            num_dict[num] = idx
            
    return '{}'.format('No matches')

def two_sum_v2(arr, num):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == num:
            return [i, j]
        if arr[i] + arr[j] < num:
            i += 1
        else:
            j -= 1
    return '{}'.format('No matches')

def two_sum_v3(lst, target):
    for el1, elem1 in enumerate(lst):
        for el2, elem2 in enumerate(lst):
            if el1 == el2:
                continue
            if elem1 + elem2 == target: 
                return [el1, el2]
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

    def test_two_sum_no_match_1(self):
        actual = two_sum_v1([2, 7, 11, -1], 20)
        expected = 'No matches'
        self.assertEqual(actual, expected)

    def test_two_sum_3(self):
        actual = two_sum_v2([2, 7, 11, 13], 9)
        expected = [0, 1] 
        self.assertEqual(actual, expected)

    def test_two_sum_4(self):
        actual = two_sum_v2([2, 7, 11, -1], 10)
        expected = [2, 3]
        self.assertEqual(actual, expected)

    def test_two_sum_no_match_2(self):
        actual = two_sum_v2([2, 7, 11, -1], 20)
        expected = 'No matches'
        self.assertEqual(actual, expected)

    def test_two_sum_5(self):
        actual = two_sum_v3([2, 7, 11, 13], 9)
        expected = [0, 1] 
        self.assertEqual(actual, expected)

    def test_two_sum_6(self):
        actual = two_sum_v3([2, 7, 11, -1], 10)
        expected = [2, 3]
        self.assertEqual(actual, expected)

    def test_two_sum_no_match_3(self):
        actual = two_sum_v3([2, 7, 11, -1], 20)
        expected = 'No matches'
        self.assertEqual(actual, expected)







unittest.main(verbosity=2)