#is_slippery
#slippery_numbers
#Fibonacci
#sum_to
#e_words
#magic_number 

##################### is_slippery ###################

'''
    >>> is_slippery(9)
    True
    >>> is_slippery(5)
    True
    >>> is_slippery(6)
    True
    >>> is_slippery(30)
    False
'''

def is_slippery(n):
    '''A "slippery number" has 3 as a factor or has 5 as a factor, but not both
    Define a method that returns a boolean indicating whether its argument is slippery.'''
    if n % 3 == 0 and n % 5 == 0:
        return False
    elif n % 3 == 0 or n % 5 == 0:
        return True
    return False 

##################### is_slippery ###################

'''
    >>> first_n_slippery_numbers(7)
    [3, 5, 6, 9, 10, 12, 18]
    >>> first_n_slippery_numbers(2)
    [3, 5]
    >>> first_n_slippery_numbers(4)
    [3, 5, 6, 9]
    >>> first_n_slippery_numbers(0)
    []
'''

def first_n_slippery_numbers(number):
    ''' Write a method that, given an integer n, returns an array of the first n slippery numbers.'''
    slippery_lst = []
    num = 0
    while len(slippery_lst) < number:
        if is_slippery(num):
            slippery_lst.append(num)
        num += 1
    return slippery_lst

##################### e_words ###################

'''
    >>> e_words('tree')
    1
    >>> e_words('Let be the finale of seem')
    3
    >>> e_words('to be or not to be')
    2
'''

def e_words(str):
    '''method return the number of words in the string that end with the letter "e"'''
    count = 0 
    for word in str.split():
        if word[-1] == 'e':
            count += 1
    return count

##################### Fibonacci ###################

'''
    >>> fibo(1)
    [0]
    >>> fibo(2)
    [0, 1]
    >>> fibo(6)
    [0, 1, 1, 2, 3, 5]
'''

def fibo(n):
    '''Define a method, #fibs, that accepts an integer as an argument. The method should return an array of the first n Fibonacci numbers'''
    fib = [0, 1]
    if n == 1:
        return [0]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

##################### Sum To ###################

'''
    >>> sum_to(3)
    6
    >>> sum_to(4)
    10
    >>> sum_to(6)
    21
'''

def sum_to(int):
    total = []
    i = 0
    while i <= int:
        total.append(i)
        i += 1   
    return sum(total)

##################### Magic Number ###################

'''
    >>> magic_numbers(3)
    [7, 16, 25]
    >>> magic_numbers(2)
    [7, 16]
    >>> magic_numbers(6)
    [7, 16, 25, 34, 43, 52]
'''

def is_magic_number(n):
    # digital sum (1+6=7 / 2+5=7)
    return (n - 1) % 9 + 1 == 7

def magic_numbers(number):
    magic_lst = []
    num = 0
    while len(magic_lst) < number: 
        if is_magic_number(num):
            magic_lst.append(num)
        num += 1
    return magic_lst





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE WORK!\n"