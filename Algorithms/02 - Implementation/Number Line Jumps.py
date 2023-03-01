#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    
    if (x1 < x2 and v1 <= v2) or (x2 < x1 and v2 <= v1):
            ans = "NO"
            
    else:
        if x1 < x2:
            while True:
                if x2 < x1:
                    ans = "NO"
                    break
                elif (x1 == x2):
                    ans = "YES"
                    break
                x1 += v1
                x2 += v2
                
        elif x2 < x1:
            while True:
                if x1 < x2:
                    ans = "NO"
                    break
                elif (x1 == x2):
                    ans = "YES"
                    break
                x1 += v1
                x2 += v2
    
    return ans

    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
