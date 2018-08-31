import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    total = meal_cost + tip + tax

    print("The total meal cost is " + str(round(total)) + " dollars.")
    
if __name__ == '__main__':

    solve(12.00, 20, 8)
