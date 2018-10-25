'''Given an array of numbers write a function that outputs 
all the prime numbers that include the second digit of my birthday'''

import unittest



def bday_prime(bday, lst):
    arr_of_primes = []
    bday_split = bday.split('/')
    second_digit = bday_split[0][1]
    for num in lst:
        if (str(second_digit) in str(num)):
            if not is_prime(num):
                continue
            else:
                arr_of_primes.append(num)

    return arr_of_primes
        
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


class Test(unittest.TestCase):

    def test_bday_prime_2(self):
        actual = bday_prime('01/08/70', [1, 21, 31, 91])
        expected = [31]
        self.assertEqual(actual, expected)

    def test_bday_prime_1(self):
        actual = bday_prime('02/08/70', [2, 22, 29, 32, 211])
        expected = [2, 29, 211]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)