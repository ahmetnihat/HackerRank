#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    if 0 < n and n <= 100:
        for i in range(n):
            print(((n - (i+1)) * " ") + ((i+1) * "#"))
    else:
        raise Exception("0 < n <= 100")
            

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
