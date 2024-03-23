#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
# s.title() fails on testcase like "w 5 3d ls"
# It capitalizes d in 3d 
def solve(s):
    res = ""
    for t in s.split(" "):
        res += t.capitalize()+ " "
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

