"""Calculate possible change from combinations of dimes and pennies.

Given an infinite supply of dimes and pennies, find the different
amounts of change can be created with exact `num_coins` coins?

For example, when num_coins = 3, you can create:

    3 = penny + penny + penny
   12 = dime + penny + penny
   21 = dime + dime + penny
   30 = dime + dime + dime

For example:

    >>> coins(0) == {0}
    True

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True


Let's make sure it works when we can spend over 10 pennies::

    >>> coins(11) == {65, 101, 38, 74, 11, 110, 47, 83, 20, 56, 92, 29}
    True

"""



def coins(num_combos):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    """
    # use set to capture unique elements
    results = set()

    # for each combination of coins make combo of dimes and pennies
    for dimes in range(num_combos + 1):
        # pennies = number of combos minus index
        # for 4: 4 - 0 = 4 pennies, 0 dimes
        # for 2: 4 - 2 = 2 pennies, 2 dimes
        pennies = num_combos - dimes
        results.add(dimes * 10 + pennies)

    return results




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAN TAKE THAT TO THE BANK!\n")
