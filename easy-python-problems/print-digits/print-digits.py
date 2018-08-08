"""Given int, print each digit in reverse order, starting with the ones place.

For example::

    >>> print_digits(1)
    1

    >>> print_digits(413)
    3
    1
    4


    >>> print_digits(7331)
    1
    3
    3
    7

"""

def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""
    # 413 % 10 -> 3
    # 413 - 3 / 10 -> 41
    # 41 % 10 -> 1
    # 41 - 1 / 10 -> 4
    while num:
        next = num % 10 
        print next
        num = (num - next) / 10



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. WOWZA!\n")
