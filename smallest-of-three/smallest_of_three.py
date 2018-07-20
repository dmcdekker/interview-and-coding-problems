'''
    >>> smallest_of_three([4, 3, 1, 2])
    6
    >>> smallest_of_three([-1, 0, -2, 3])
    0
    >>> smallest_of_three([10, 0, 11, 9])
    0
    >>> smallest_of_three([-5, -2, 1, 9])
    -18
'''


def smallest_of_three(arr):
    '''Find the smallest product of three'''
    init_product_of_three = arr[0] * arr[1] * arr[2]
    if 0 in arr: return 0
    for i in range(0, len(arr)-2):
        for j in range(i + 1, len(arr)-1):
            for k in range(j + 1, len(arr)):
                min_product = min(init_product_of_three, arr[i] * arr[j] * arr[k])
 
    return min_product

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. RIGHT ON!\n")