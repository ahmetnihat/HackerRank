#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    time = s[-2:]
    hours = s[:2]
    
    if time == "PM":
        if hours != "12":
            hours = int(hours)
            hours += 12
            
    if time == "AM":
        if hours == "12":
            hours = "00"
            
    result = ''
    result += str(hours)
    result += s[2:-2]
    
    return result
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
