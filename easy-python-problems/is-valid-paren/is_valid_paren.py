import unittest

def is_valid(string):
    '''Check if string contains balanced parens'''
    
    if not string:
        raise ValueError('Empty String')
    paren_dict = {')':'(', ']':'[', '}':'{'}
    stack = []
    for paren in string:
        if paren in paren_dict.values():
            stack.append(paren)
        elif paren in paren_dict:
            if not stack or paren_dict[paren] != stack.pop():
                return False
    return not stack

class Test(unittest.TestCase):
    def test_is_valid_1(self):
        actual = is_valid('{{}}')
        expected = True
        self.assertEqual(actual, expected)

    def test_is_valid_2(self):
        actual = is_valid('{}[')
        expected = False
        self.assertEqual(actual, expected)

    def test_is_valid_3(self):
        actual = is_valid('][]')
        expected = False
        self.assertEqual(actual, expected)

    def test_is_valid_4(self):
        actual = is_valid('[]{}()')
        expected = True
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)





