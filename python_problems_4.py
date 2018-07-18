#sum_to_zero
#no_space
#repeat_str
#array_plus_array
#multiple_of_index
#reverse_seq
#two_sum
#largest_factor
#rubyify
#find_factors
#pizza_slices
#three_digit_format

#################### Sum To Zero ###################

# '''
#     >>> sum_to_zero([3, 1, -3])
#     True
#     >>> sum_to_zero([4, 1, 5])
#     False
#     >>> sum_to_zero([-5, 5, 2])
#     True
# '''

# def sum_to_zero(lst_of_nums):
#     '''Do any two numbers add to zero?''' 
#     set_of_nums = set(lst_of_nums)
#     for num in set_of_nums:
#         if -(num) in set_of_nums:
#             return True
#     return False

# ################### No Space ###################

# '''
#     >>> no_space('bcbcbc b nh nk  ')
#     'bcbcbcbnhnk'
#     >>> no_space('x        x')
#     'xx'
# '''

# def no_space(string):
#     '''Take out all white space in a string'''
#     no_space_str = string.split(' ')
#     return ''.join(no_space_str)

# ##################### Repeat String ###################

# '''
#     >>> repeat_str(2, 'x')
#     'xx'
#     >>> repeat_str(5, '*')
#     '*****'
# '''

# def repeat_str (n, s):
#   return s * n

# #################### Array Plus Array ###################

# '''
#     >>> array_plus_array([1, 2, 3], [4, 5, 6]) 
#     21
#     >>> array_plus_array([0, 1, 5], [5, 8, 10])
#     29
# '''

# def array_plus_array(arr1, arr2):
#     return sum(arr1) + sum(arr2)

# #################### Multiple of Index ###################

# '''
#     >>> multiple_of_index([22, -6, 32, 82, 9, 25])
#     [-6, 32, 25]
#     >>> multiple_of_index([68, -1, 1, -7, 10, 20])
#     [-1, 20]
#     >>> multiple_of_index([28,38,-44,-99,-13,-54,77,-51])
#     [38, -44, -99]
# '''

# def multiple_of_index(lst_of_nums):
#     '''Return numbers in a list that are divisible by their index'''
#     multiply_num_by_idx = []
#     for idx, num in enumerate(lst_of_nums):
#         if idx != 0 and num % idx == 0:
#             multiply_num_by_idx.append(num)
#     return multiply_num_by_idx

# #################### Reverse Sequence ###################

# '''    
#     >>> reverse_sequence(5)
#     [5, 4, 3, 2, 1]
#     >>> reverse_sequence(4)
#     [4, 3, 2, 1]
# '''

# def reverse_sequence(number):
#     lst_of_nums = []
#     for num in range(1, number + 1):
#         lst_of_nums.append(num)
#     return lst_of_nums[::-1]

# #################### Two Sum ###################

# '''
#     >>> two_sum([1, 2, 3, 4, 5], 8)
#     True
#     >>> two_sum([1, 2, 3, 4, 5, 6], 18) 
#     False
#     >>> two_sum([1, 3, 6], 6)
#     False
#     >>> two_sum([1, 8, 2, 1], 0)
#     False
# '''

# def two_sum(lst, target):
#     '''Return true if the sum of any two elements equal the target number'''
#     for el1, elem1 in enumerate(lst):
#         for el2, elem2 in enumerate(lst):
#             if el1 == el2:
#                 continue
#             if elem1 + elem2 == target: 
#                 return True 
#     return False

# #################### Largest Factor ###################

# '''
#     >>> largest_factor(10)
#     5
#     >>> largest_factor(143)
#     13
#     >>> largest_factor(27)
#     9
#     >>> largest_factor(17)
#     1
# '''

# def largest_factor(number):
#     factor = number - 1
#     while factor < number:
#         if number % factor == 0:
#             break
#         factor -= 1
#     return factor

# #################### Largest Prime ###################

'''
    >>> largest_prime_factor(10)
    5
    >>> largest_prime_factor(143)
    13
    >>> largest_prime_factor(27)
    9
    >>> largest_prime_factor(21)
    7
'''

def largest_prime_factor(number):
    factor = 2
    while (factor * factor) < number:
        if number % factor == 0:
            number /= factor
        factor += 1
    return number        

##################### Tests ###################

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE ONE!\n"