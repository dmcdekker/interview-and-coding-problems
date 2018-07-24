"""Convert a decimal number to binary representation.

    >>> dec2bin_division(0)
    '0'

    >>> dec2bin_division(1)
    '1'

    >>> dec2bin_division(2)
    '10'

    >>> dec2bin_division(4)
    '100'

    >>> dec2bin_division(15)
    '1111'
"""

def dec2bin_division(num):
    """Convert a decimal number to binary representation."""
    if num == 0:
        return '0'
    binary_digits = []
    while num > 0:
        binary_digits.append(str(num % 2))
        num /= 2
    return ''.join(reversed(binary_digits))



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. W00T!\n")
