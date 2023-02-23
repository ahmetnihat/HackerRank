#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    count = 0
    count_list = []
    
    for i in arr:
        count += i
        
    for j in arr:
        count_list.append((count - j))
    
    count_list.sort()
    
    return print(count_list[0], count_list[-1])
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
