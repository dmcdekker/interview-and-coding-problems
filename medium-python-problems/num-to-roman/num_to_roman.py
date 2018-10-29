import unittest

roman = { 'M': 1000, 'CM': 900, 'D': 500,
    'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL':40,  'X': 10,
    'IX': 9, 'V': 5, 'IV': 4, 'I': 1}


def int_to_roman(number):
    '''Convert Roman number to Arabic'''
    result = ''
    roman_numerals = ''
    for numeral, value in roman.items():
        # go through roman dict to find value 
        while number >= value:
            # add to result
            result += numeral
            # minus value from number 
            number -= value
    return result

def roman_to_int(s):
    '''Convert Arabic number to Roman'''
    result = 0
    for i in range(0, len(s)-1):
        # if current value is less than next: subtract from result
        if roman[s[i]] < roman[s[i+1]]:
            result -= roman[s[i]]
        else:
            # otherwise add it
            result += roman[s[i]]
    # add last number 
    result += roman[s[-1]]
    return result

class Test(unittest.TestCase):

    def test_int_to_roman_1(self):
        actual = int_to_roman(25)
        expected = 'XXV'
        self.assertEqual(actual, expected)

    def test_int_to_roman_2(self):
        actual = int_to_roman(4)
        expected = 'IV'
        self.assertEqual(actual, expected)

    def test_int_to_roman_3(self):
        actual = int_to_roman(29)
        expected = 'XXIX'
        self.assertEqual(actual, expected)

    def test_roman_to_int_1(self):
        actual = roman_to_int('XXV')
        expected = 25
        self.assertEqual(actual, expected)

    def test_roman_to_int_2(self):
        actual = roman_to_int('IV')
        expected = 4
        self.assertEqual(actual, expected)

    def test_roman_to_int_3(self):
        actual = roman_to_int("XXIX")
        expected = 29
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)

