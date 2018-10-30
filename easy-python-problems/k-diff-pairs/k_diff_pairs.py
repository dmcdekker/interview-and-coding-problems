import unittest
import collections



def find_pairs_1(nums, k):
    lst_tupes = set()
    for idx1, num1 in enumerate(nums):
        for idx2, num2 in enumerate(nums):
            diff = abs(num1 - num2)
            if diff == k and idx1 != idx2:
                if num1 != num2 and (num2, num1) not in lst_tupes:
                    lst_tupes.add((num1, num2))
                elif num1 == num2:
                    lst_tupes.add((num1, num2))


    return len(lst_tupes)

    
def find_pairs_2(nums, diff):
    result = 0
    count_nums = collections.Counter(nums)
    for number in count_nums:
        # if the diff is > 0 and the number plus diff is in count nums
        # or if diff == 0 and there is more than one occurence of the same number
        if diff > 0 and number + diff in count_nums or diff == 0 and count_nums[number] > 1:
            result += 1
    return result

class Test(unittest.TestCase):

    def test_find_pairs_1(self):
        actual = find_pairs_1([3, 1, 4, 1, 5], 2)
        expected = 2
        self.assertEqual(actual, expected)

    def test_find_pairs_2(self):
        actual = find_pairs_1([1, 3, 1, 5, 4], 0)
        expected = 1
        self.assertEqual(actual, expected)

    def test_find_pairs_3(self):
        actual = find_pairs_2([3, 1, 4, 1, 5], 2)
        expected = 2
        self.assertEqual(actual, expected)

    def test_find_pairs_4(self):
        actual = find_pairs_2([1, 3, 1, 5, 4], 0)
        expected = 1
        self.assertEqual(actual, expected)




unittest.main(verbosity=2)

