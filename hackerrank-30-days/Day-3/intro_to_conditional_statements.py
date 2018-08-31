import math
import os
import random
import re
import sys

if __name__ == '__main__':

    N = 3
    if (N % 2) != 0:
        print("Weird")
    else:
        if N <= 5 or N > 20:
            print("Not Weird")
        else:
            print("Weird") 