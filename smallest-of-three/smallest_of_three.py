'''
    >>> smallest_of_three([4, 3, 1, 2])
    6
    >>> smallest_of_three([-1, 0, -2, 3])
    0
    >>> smallest_of_three([1, 28, 2, 1])
    2
    >>> smallest_of_three([-5, -2, 1, 9])
    -45
    >>> smallest_of_three([-1, 0, -2, 3])
    0
'''


def smallest_of_three(arr):
    '''Find the smallest product of three integers'''
    sorted_arr = sorted(arr) 
    return min(sorted_arr[0] * sorted_arr[1] * sorted_arr[2],
               sorted_arr[0] * sorted_arr[-2] * sorted_arr[-1])

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. RIGHT ON!\n")