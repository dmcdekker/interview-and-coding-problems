import unittest


def is_single_riffle(half1, half2, shuffled_deck):
    '''write a function to tell us if a full deck of cards shuffled_deck is a single riffle of two other halves half1 and half2'''
    # point to halves
    h1 = 0 # top half
    h2 = 0 # bottom half
    # iterate over cards in shuffled deck
    for card in shuffled_deck:
        # if current card is the same as top half card
        if h1 < len(half1) and card == half1[h1]:
            h1 += 1
        # if current card is the same as bottom half card
        elif h2 < len(half2) and card == half2[h2]:
            h2 += 1
        else:
            return False
    return True

# Tests

class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)