import unittest
from functools import reduce

def sum_except_current(lst):
    result = []
    for idx1, num1 in enumerate(lst):
        curr_sum = 1
        for idx2, num2 in enumerate(lst):
            if idx2 != idx1:
                curr_sum *= num2
        result.append(curr_sum)
    return result

def sum_except_current_1(lst):
    result = []
    curr_sum = 1
    for idx1, num1 in enumerate(lst):
        curr_sum *= reduce((lambda x, y: x * y), lst)
        result.append(curr_sum // num1)
    return result

print(sum_except_current_1([1, 2, 3, 4, 5]))

class Test(unittest.TestCase):

    def test_sum_except_current_1(self):
        actual = sum_except_current_1([1, 2, 3, 4, 5])
        expected = [120, 60, 40, 30, 24]
        self.assertEqual(actual, expected)

    def test_sum_except_current_2(self):
        actual = sum_except_current_1([1, 3, 5, 7, 9])
        expected = [945, 315, 189, 135, 105]
        self.assertEqual(actual, expected)

    def test_sum_except_current_3(self):
        actual = sum_except_current_2([1, 2, 3, 4, 5])
        expected = [120, 60, 40, 30, 24]
        self.assertEqual(actual, expected)

    def test_sum_except_current_4(self):
        actual = sum_except_current_2([1, 3, 5, 7, 9])
        expected = [945, 315, 189, 135, 105]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)