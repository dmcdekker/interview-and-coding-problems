"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10], 10)
    8
    >>> missing_number([7, 3, 2, 4, 5, 6, 1, 9, 10, 8], 10)
    'No numbers missing'
    
    """
    num_set = set(nums)
    for num in range(1, max_num + 1):
        if num not in num_set:
            return num
    return '{}'.format('No numbers missing')        


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print ("\n*** ALL TESTS PASS. NICELY DONE!\n")
