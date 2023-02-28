#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countFruit(s, t, fruit_distance_list):
    
    sams_fruit = 0
    
    for fruit_distance in fruit_distance_list:
        if s <= fruit_distance and fruit_distance <= t:
            sams_fruit += 1
    
    return sams_fruit

            
            
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    
    apples_distance = [(a + apple) for apple in apples]
    oranges_distance = [(b + orange) for orange in oranges]
    
    print(f"{countFruit(s, t, apples_distance)}\n{countFruit(s, t, oranges_distance)}")
    
        
    
    
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
