#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
#If a[i] > b[i], then Alice is awarded 1 point.
#If a[i] < b[i], then Bob is awarded 1 point.
#If a[i] = b[i], then neither person receives a point.
def compareTriplets(a, b):
    alice = 0 
    bob = 0
    for i in range(len(a)):
        if (a[i] > b[i]):
            alice += 1
        elif (a[i] < b[i]):
            bob += 1   
        elif (a[i] == b[i]):
            continue
    result = [alice, bob]
    return result        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
