import unittest

def matching_strings(strings, queries):
    result = [] 
    for q in queries: 
        result.append(strings.count(q)) 
    return result

class Test(unittest.TestCase):

    def test_matching_strings_1(self):
        actual = matching_strings(['def','de', 'fgh'], ['de', 'lmn', 'fgh'])
        expected = [1, 0, 1] 
        self.assertEqual(actual, expected)

    def test_matching_strings_2(self):
        actual = matching_strings(['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 
                                    'sdaklfj', 'asdjf', 'na', 'asdjf', 'na',
                                    'basdn', 'sdaklfj', 'asdjf'], ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn'])
        expected = [1, 3, 4, 3, 2] 
        self.assertEqual(actual, expected)

    def test_matching_strings_3(self):
        actual = matching_strings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab'])
        expected = [2, 1, 0] 
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)