# import math
# import os
# import random
# import re
# import sys

# if __name__ == '__main__':
#     n = int(input()) 
#     arr = list(map(int, input().rstrip().split()))
#     print(" ".join(map(str, arr[::-1])))

def reverse_string(str_in):
    str_lst = list(str_in)
    str_out = ''
    for letter in str_lst[::-1]:
        str_out += letter
    return str_out


print(reverse_string('reversethis'))