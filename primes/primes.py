"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""

def primes(count):
    """Return count number of prime numbers, starting at 2."""
    prime_list = []
    idx = 2
    while count != len(prime_list):
        for i in range(2, int(idx ** 0.5) + 1):
            if idx % i == 0:
                break
        else:
            prime_list.append(idx)
        idx += 1
    return prime_list


# another way
# def primes(count):
#     """Return count number of prime numbers, starting at 2."""
#     primes = []
#     num = 2

#     while len(primes) != count:

#         if is_prime(num):
#             primes.append(num)

#         num += 1

#     return primes

# def is_prime(num):
    
#     if num < 2:
#         return False

#     # definition: 2 is prime
#     if num == 2:
#         return True

#     # not divisable by 2
#     if num % 2 == 0:
#         return False

#     # see if number is prime -- we'll do this by checking
#     # to see if there's any odd number 3 .. sqrt(num)
#     # that evenly divides num (why square root? think about it!)

#     n = 3

#     while n * n <= num:
#         if num % n == 0:
#             return False
#         # Go to next odd number
#         n += 2

#     return True




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
