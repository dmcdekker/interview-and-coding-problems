#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    for idx in range(6):
       arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
       arr.append(arr_t)

    def max_hourglasses(arr):
        max = None        
        for i in range(0, 4):
            for j in range(0, 4):
                sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                  arr[i+1][j+1] + \
                  arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                if max == None or sum > max:
                    max = sum
        return max

print(max_hourglasses(arr))
        