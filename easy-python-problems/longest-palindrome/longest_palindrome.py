import unittest

def substrings(s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        results = []
        # generate substrings (start at end index, end at index 0, step -1)
        for substring in range(length, 0, -1):
            for index in range(length - substring + 1):
                results.append(s[index: index+substring])
        return results

# helper function to decide if substring is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# get longest string 
def longest_palindrome(string):
    for longest in substrings(string):
        if is_palindrome(longest):
            return longest



class Test(unittest.TestCase):

    def test_longest_palindrome_1(self):
        actual = longest_palindrome('babad')
        expected = 'bab'
        self.assertEqual(actual, expected)

    def test_longest_palindrome_2(self):
        actual = longest_palindrome('ilikeitttttl')
        expected = 'ttttt'
        self.assertEqual(actual, expected)

    def test_longest_palindrome_3(self):
        actual = longest_palindrome('helloforever')
        expected = 'rever'
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)