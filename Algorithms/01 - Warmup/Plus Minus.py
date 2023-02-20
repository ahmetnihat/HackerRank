#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import Decimal

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p = 0
    ng = 0
    ze = 0
    n = len(arr)
    
    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            ng += 1
        else:
            ze += 1
            
    p_result = round(Decimal((p / n)), 6)
    ng_result = round(Decimal((ng / n)), 6)
    ze_result = round(Decimal((ze / n)), 6)
    
    print(p_result, "\n", ng_result, "\n", ze_result)
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
