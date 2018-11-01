import unittest

def wildcard_string(str1, str2):

    front = ''
    back = ''
    str1_len = 0

    for idx, val in enumerate(str1):
        if not val.isalpha():
            idx_number = idx
            wildcard_number = int(val)
            front = str1[:idx_number]
            back = str1[idx_number + 1:]
            str1_len = len(front) + len(back)
        if front and back in str2 and len(str2) == str1_len + wildcard_number:
            return True
    return False
    
class Test(unittest.TestCase):

    def test_wildcard_string_1(self):
        actual = wildcard_string('d3dog', 'datadog')
        expected = True
        self.assertEqual(actual, expected)

    def test_wildcard_string_2(self):
        actual = wildcard_string('da1adog', 'datadog')
        expected = True
        self.assertEqual(actual, expected)

    def test_wildcard_string_3(self):
        actual = wildcard_string('da4g', 'datadog')
        expected = True
        self.assertEqual(actual, expected)

    def test_wildcard_string_4(self):
        actual = wildcard_string('data2g', 'datadogz')
        expected = False
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
            
