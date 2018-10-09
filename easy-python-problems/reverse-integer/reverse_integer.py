import unittest
# Assume we are dealing with an environment which could only store integers 
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose 
# of this problem, assume that your function returns 0 when the reversed integer 
# overflows.

'''Given a 32-bit signed integer, reverse digits of an integer.'''

def reverse(num):
        """
        :type x: int
        :rtype: int
        """
        rev_str = str(num)[::-1]
        if rev_str[-1] is '-':
            rev_str = int(rev_str.replace('-', '')) * (-1)
        return int(rev_str) if int(rev_str) >= -2**31 and int(rev_str) <= (2**31)-1 else 0

class Test(unittest.TestCase):

    def test_reverse_1(self):
        actual = reverse(321)
        expected = 123
        self.assertEqual(actual, expected)

    def test_reverse_2(self):
        actual = reverse(1234567891)
        expected = 1987654321
        self.assertEqual(actual, expected)

    def test_reverse_2(self):
        actual = reverse(-123)
        expected = -321
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)