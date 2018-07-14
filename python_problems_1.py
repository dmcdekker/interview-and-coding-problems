# this file contains lots of smaller problems
#crazy_sum
#square_nums
#crazy_nums
#palindrome
#wild_sum
#lucky_number
#oddball_sum 
#disemvowel

##################### Crazy Sum ###################

'''
    >>> crazy_sum([2])
    0
    >>> crazy_sum([2, 3])
    3
    >>> crazy_sum([2, 3, 5])
    13
    >>> crazy_sum([2, 3, 5, 2])
    19
'''

def crazy_sum(numbers):
    '''Multiply number by index and sum total'''
    sum = 0
    index = 0
    while index < len(numbers):
        sum += numbers[index] * index
        index += 1
    return sum


#################### Square Nums ###################

'''
    >>> square_nums(5)
    2
    >>> square_nums(10)
    3
    >>> square_nums(25)
    4
'''

def square_nums(max):
    '''Find max square number'''
    num = 0
    idx = 1
    while idx*idx < max:
        num += 1
        idx += 1
    return num 

##################### Crazy Nums ###################

'''
    >>> crazy_nums(20)
    [3, 5, 6, 9, 10, 12, 18]
    >>> crazy_nums(10)
    [3, 5, 6, 9]
    >>> crazy_nums(3)
    []
'''

def crazy_nums(number):
    '''Find numbers divisible by 3 or 5 but not both'''
    divisible_list = []
    for num in range(1, number):
        if num % 3 and num % 5:
            continue
        elif num % 3 or num % 5:
            divisible_list.append(num)
    return divisible_list


##################### Palindrome_1 ###################

'''
    >>> is_palindrome_1('racecar')
    True
    >>> is_palindrome_1('noon')
    True
    >>> is_palindrome_1('notme')
    False
'''

def is_palindrome_1(string):
    '''Return true if string is a palindrome'''
    first = 0
    last = -1
    while first < len(string)/2:
        if string[first] != string[last]:
            return False
        first += 1
        last -= 1
    return True


##################### Palindrome_2 ###################

'''
    >>> is_palindrome_2('racecar')
    True
    >>> is_palindrome_2('noon')
    True
    >>> is_palindrome_2('notme')
    False
'''

def is_palindrome_2(string):
    '''Return true if string is a palindrome'''
    for letter in range(0, len(string)/2):
        if string[letter] != string[len(string)-letter-1]:
            return False
    return True


##################### Wild Sum ###################

'''
    >>> wild_sum(0)
    0
    >>> wild_sum(2)
    0
    >>> wild_sum(3)
    2
    >>> wild_sum(7)
    9
'''

def wild_sum(number):
    '''Define a method that sums all the numbers less than n that are:
        Divisible by 2 or divisible by 3, but not divisible by both
    '''
    sum = 0
    for num in range(1, number):
        if num % 2 and num % 3:
            continue
        elif num % 2 or num % 3:
            sum += num 
    return sum


##################### Lucky Seven ###################

'''
    >>> lucky_number([2, 1, 5, 1, 0], 7)
    True
    >>> lucky_number([0, -2, 1, 8], 6)
    False
    >>> lucky_number([6, 7, 7, 7], 21)
    True
    >>> lucky_number([3, 4, 3, 4], 7)
    False
'''

def lucky_number(lst, number):
    '''Return true if the sum of 3 consecutive numbers == number'''
    for num in range(0, len(lst) - 2):
        three_nums = lst[num:num+3]
        if sum(three_nums) == number:
            return True
    print False

##################### Odd Sums ###################

'''
    >>> odd_sum([1, 2, 3, 4, 5])
    9
    >>> odd_sum([0, 6, 4, 4])
    0
    >>> odd_sum([7, 7, 7, 7])
    28
    >>> odd_sum([1, 2, 1])
    2
'''

def odd_sum(numbers):
    '''Accepts array of numbers and returns sum of all odd elements'''
    total = 0
    for num in numbers:
        if (num % 2) == 1:
            total = total + num
    return total

##################### Disemvowel ###################

'''
    >>> disemvowel('foobar')
    'fbr'
    >>> disemvowel("ruby")
    'rby'
    >>> disemvowel("aeiou")
    ''
'''

def disemvowel(string):
    result = ''
    vowels = ('a', 'e', 'i', 'o', 'u')
    for letter in string:
        if letter not in vowels:
            result += letter
    return result



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE WORK!\n"