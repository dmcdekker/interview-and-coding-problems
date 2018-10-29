import unittest

def length_of_longest_substring_no_repeats(string):
        """
        :type s: str
        :rtype: int
        """
        # O(n^2)
        results = []
        for substring in range(len(string) + 1):
            for index in range(len(string)+ 1 - substring):
                word = string[index: index + substring]
                if len(word) == len(set(word)):
                    results.append(word)
        return len(sorted(results, key=len)[-1])

        # Hackbright solution
        # keep track of longest substring
        # longest = 0
        # for index in range(len(s)):
        #     # use set for unique chars
        #     seen = set()
        #     # keep track while going along: look at each substring
        #     for letter in s[index:]:
        #         if letter in seen:
        #             break
        #         # add if not in seen
        #         seen.add(letter)
        #     longest = max(longest, len(seen))
        # return longest

class Test(unittest.TestCase):

    def test_longest_substring_1(self):
        actual = length_of_longest_substring_no_repeats('abcabcbb')
        expected = 3
        self.assertEqual(actual, expected)

    def test_longest_substring_2(self):
        actual = length_of_longest_substring_no_repeats('ilikeitttttl')
        expected = 4
        self.assertEqual(actual, expected)

    def test_longest_substring_3(self):
        actual = length_of_longest_substring_no_repeats('helloforever')
        expected = 5
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)