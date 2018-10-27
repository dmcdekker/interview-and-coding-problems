import unittest

def number_is_palindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        new_arr = []
        while x:
            num = x % 10
            new_arr.append(int(num))
            x = (x - num) / 10

        return new_arr == new_arr[::-1]

class Test(unittest.TestCase):
    def test_num_is_palindrome_1(self):
        actual = number_is_palindrome(121)
        expected = True
        self.assertEqual(actual, expected)

    def test_num_is_palindrome_2(self):
        actual = number_is_palindrome(12231)
        expected = False
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
