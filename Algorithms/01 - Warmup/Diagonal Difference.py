#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    arr_sag = 0
    arr_sol = 0
    count = 0
    
    for i in range(0, len(arr[0])):
        count -= 1
        arr_sag += arr[i][i]
        arr_sol += arr[i][count]
    
    result = arr_sag - arr_sol
    
    if  result < 0:
        result = result * (-1)
    
    return result
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
