def get_max_profit(stock_prices):
    '''Write an efficient function that takes stock_prices and 
       returns the best profit I could have made from one purchase 
       and one sale of one share of Apple stock yesterday.'''
       
    # set min price
    min_price = stock_prices[0]
    # Calculate the max profit
    max_profit = stock_prices[1] - stock_prices[0]
    
    # error message if less than 2 values
    if len(stock_prices) <= 1:
        raise ValueError('Need at least 2 prices')
    # iterate through list of prices
    for current_time in range(1, len(stock_prices)):
        # set current price
        current_price = stock_prices[current_time]
        # potential profit for each item
        potential_profit = current_price - min_price
        # store largest value of max profit
        max_profit = max(max_profit, potential_profit)
        # store smallest value of price
        min_price = min(min_price, current_price)
        
    return max_profit

# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_price_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([1])

    def test_empty_list_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([])

unittest.main(verbosity=2)