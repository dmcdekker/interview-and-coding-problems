"""Convert a hexadecimal string, like '1A', into it's decimal equivalent.

    >>> hex_convert('6')
    6

    >>> hex_convert('10')
    16

    >>> hex_convert('FF')
    255

    >>> hex_convert('FFFF')
    65535
"""


def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent."""
    HEX_DICT = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, 
                '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12,
                'D':13, 'E':14, 'F':15}

    result = 0
    # enumerate to add indices
    for i, hex_char in enumerate(hex_in):
        # go through each element in string and find in dict
        hex_digit = HEX_DICT[hex_char]
        # multiply each element by 16^i (16^0, 16^1)
        power = 16 ** (len(hex_in) - i - 1)
        # add together each hex_digit * power
        result += hex_digit * power

    return result

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n")
