"""Reverse list in place.

You cannot do this with reversed(), .reverse(), or list slice
assignment!

    >>> lst = []
    >>> rev_list_in_place(lst)
    >>> lst
    []

    >>> lst = ['a']
    >>> rev_list_in_place(lst)
    >>> lst
    ['a']

    >>> lst = [1, 2, 3]
    >>> rev_list_in_place(lst)
    >>> lst
    [3, 2, 1]

    >>> lst = [1, 2, 3, 4]
    >>> rev_list_in_place(lst)
    >>> lst
    [4, 3, 2, 1]
"""


def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice
    assignment!
    """
    for idx in range(len(lst)//2):
        lst[idx], lst[-idx-1] = lst[-idx-1], lst[idx]

'''Alt solution'''

def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice
    assignment!
    """
    
    # list
    # 1 2 3 4 5
    # 5 2 3 4 1
    # 5 4 3 2 1

    # intializing pointers
    left = 0
    right = len(lst)-1

    # condition for termination
    while left < right:
        # temp variable assigned to value of left
        temp = lst[left]
        # swap values
        lst[left] = lst[right]
        # right variable assigned to original left val
        lst[right] = temp

        # move pointers
        left += 1
        right -= 1


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE THE BEST!\n")
