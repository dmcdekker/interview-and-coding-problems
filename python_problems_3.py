#reverse_digits
#pair_product
#slice_between_vowels
#array_times_two (don't modify array)
#array_times_twoo (modify array)
#redact_five_letter_words
#largest_pair
#boolean_to_binary
#third_largest
#time_conversion

##################### Reverse Digits ###################

'''
    >>> reverse_digits(5)
    [5, 4, 3, 2, 1]
    >>> reverse_digits(10)
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> reverse_digits(1)
    [1]
'''

def reverse_digits(number):
    '''Define a method that reverses the digits of its argument and returns the resulting list of numbers'''
    rev_lst = []
    for num in range(1, number + 1):
        rev_lst.append(num)
    return rev_lst[::-1]



##################### Pair Product ###################

'''
    >>> pair_product([3, 1, 5], 15)
    True
    >>> pair_product([4, 1, 5], 20)
    True
    >>> pair_product([5, 5, 2], 30)
    False
'''    

def pair_product(arr, target_product):
    '''Define a method, that accepts two arguments: a list of integers and a target_product (an integer). The method returns a boolean indicating whether any pair of elements in the array multiplied together equals that product'''
    for idx1 in range(0, len(arr)):
        for idx2 in range(0, len(arr)):
            if arr[idx1] * arr[idx2] == target_product:
                return True
    return False
    

##################### Slice Between Vowels ###################

'''
    >>> slice_between_vowels('serendipity')
    'rendip'
    >>> slice_between_vowels('train')
    ''
    >>> slice_between_vowels('dog')
    ''
    >>> slice_between_vowels('refrain')
    'fr'
'''

def slice_between_vowels(word):
    '''Return the slice of the word between the first and last vowels of that word. Return an empty string if the word has less than 2 vowels'''
    vowels = ('a', 'e', 'i', 'o', 'u')
    first_idx = 0
    last_idx = -1
    for letter in word.split():
        if letter in vowels:
            word[first_idx]
            word[last_idx]
        first_idx += 1 
        last_idx -= 1
    return word[first_idx + 1: last_idx - 1]

##################### Array Times Two ###################

'''
    >>> array_times_two([2, 3, 4])
    [4, 6, 8]
    >>> array_times_two([15, 22, 34])
    [30, 44, 68]
'''

def array_times_two(lst):
    '''Given an array of numbers, returns another array with each of the argument's numbers multiplied by two. Do not modify the original array'''
    lst_times_two = []
    for num in lst:
        lst_times_two.append(num * 2)
    return lst_times_two

##################### Array Times Twoo ###################

'''
    >>> array_times_twoo([2, 3, 4])
    [4, 6, 8]
    >>> array_times_twoo([15, 22, 34])
    [30, 44, 68]
'''

def array_times_twoo(lst):
    '''given an array of numbers, mulitplies each of its elements by two. This SHOULD mutate the original array'''
    for idx, num in enumerate(lst):
        lst[idx] = num * 2
    return lst

##################### Redact 5 letter word ###################

'''
    >>> redact_five_letter_words('long longer longest longy')
    'long longer longest #####'
    >>> redact_five_letter_words('denis hello world')
    '##### ##### #####'
'''
def redact_five_letter_words(string):
    '''Define a method that substitutes all five-letter words in its argument with "#####" and returns the result. Do not consider punctuation.'''
    new_str = []
    for word in string.split():
        if len(word) == 5:
            new_str.append('#####')
        else:
            new_str.append(word)
    return ' '.join(new_str)


##################### Largest Pair ###################

'''
    >>> largest_pair([[-4, 0],[-2,-1],[-3,2]])
    [-3, 2]
    >>> largest_pair([[4, 0],[2,-1],[-3,-2]])
    [4, 0]
    >>> largest_pair([[1, 0]])
    [1, 0]
'''

def largest_pair(pairs_lst):
    largest = pairs_lst[0]
    for pair in pairs_lst:
        if (largest[0], largest[1]) < (pair[0], pair[1]):
            largest = pairs_lst[pair[0] + pair[1]]
    return largest


##################### Boolean to Binary ###################

'''
    >>> boolean_to_binary([True])
    '1'
    >>> boolean_to_binary([True, False, True])
    '101'
    >>> boolean_to_binary([False, False, True, False])
    '0010'
'''

def boolean_to_binary(boolean_lst):
    '''Define a method that accepts an array of booleans as an argument. Your method should convert the array into a string of 1's (for true values) and 0's (for false values) and return the result'''
    binary_string = ''
    for boolean in boolean_lst:
        if boolean == True:
            binary_string += '1'
        elif boolean == False:
            binary_string += '0'
    return binary_string

##################### Third Largest ###################

'''
    >>> third_largest([5, 9, 9, 3, 7, 7, 2, 10])
    7
    >>> third_largest([5, 10, 3])
    3
'''

def third_largest(lst):
    '''Define a method that returns the third-largest element in an array (assume at least 3 elems)'''
    nums_dict = {}
    for num in lst:
        nums_dict[num] = nums_dict.get(num, 0) + 1
    sorted_dict = sorted((key, val) for key, val in nums_dict.items())
    print sorted_dict
    # return 3rd largest key (key in first place)
    return sorted_dict[-3][0]

##################### Date TIme Conversion ###################

'''
    >>> time_conversion(60)
    '01:00'
    >>> time_conversion(20)
    '00:20'
    >>> time_conversion(160)
    '02:40'
'''
def time_conversion(minutes):
    '''Define a method that takes a number of minutes as its argument and returns a string formatted HH:MM'''
    hour = minutes / 60
    mins = minutes % 60
    return '{}:{}'.format('%02d' % hour, '%02d' % mins)


# ##################### Tests ###################

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE ONE!\n"