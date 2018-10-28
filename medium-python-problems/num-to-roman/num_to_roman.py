import unittest

def test_int_to_roman(number):
    ROMAN_NUMERAL_TABLE = { 'M': 1000, 'CM': 900, 'D': 500,
    'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL':40,  'X': 10,
    'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    roman_numerals = ''
    for numeral, value in ROMAN_NUMERAL_TABLE.items():
        # divide num by values in dict for 25: (2 * 10, 1 * 5)
        count = (number // value)
        # subtract for 25:(2 * 10, 1 * 5)
        number -= (count * value)
        # add numeral number of times to table
        roman_numerals += (numeral * count)

    return roman_numerals

class Test(unittest.TestCase):

    def test_int_to_roman_1(self):
        actual = test_int_to_roman(25)
        expected = 'XXV'

    def test_int_to_roman_2(self):
        actual = test_int_to_roman(4)
        expected = 'IV'

    def test_int_to_roman_3(self):
        actual = test_int_to_roman(29)
        expected = 'XXIX'

unittest.main(verbosity=2)

