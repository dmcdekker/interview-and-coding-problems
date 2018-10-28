import unittest

def longest_common_prefix_1(strs):
    if not strs:
        return ''
    longest = strs[0]
    # start at second index
    for string in strs[1:]:
        index = 0
        # while not indexing out and previous chars are equal at the same indices
        while index < len(string) and index < len(longest) and string[index] == longest[index]:
            index += 1

        # longest assigned to the string up to     
        longest = longest[:index]
    return longest

def longest_common_prefix_2(strs):
    if not strs:
        return ''
    longest = strs[0]
    for idx in range(len(longest)):
        for word in strs[1:]:
            if idx >= len(word) or longest[idx] != word[idx]:
                return longest[:idx]

    return longest

class Test(unittest.TestCase):
    
    def test_lcp_1(self):
        actual = longest_common_prefix_1(["flower","flow","flight"])
        expected = 'fl'
        self.assertEqual(actual, expected)

    def test_lcp_2(self):
        actual = longest_common_prefix_1(["hello","heavy","healing"])
        expected = 'he'
        self.assertEqual(actual, expected)

    def test_lcp_3(self):
        actual = longest_common_prefix_1(["look","loom","loose"])
        expected = 'loo'
        self.assertEqual(actual, expected)

    def test_lcp_4(self):
        actual = longest_common_prefix_2(["flower","flow","flight"])
        expected = 'fl'
        self.assertEqual(actual, expected)

    def test_lcp_5(self):
        actual = longest_common_prefix_2(["hello","heavy","healing"])
        expected = 'he'
        self.assertEqual(actual, expected)

    def test_lcp_6(self):
        actual = longest_common_prefix_2(["look","loom","loose"])
        expected = 'loo'
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)





