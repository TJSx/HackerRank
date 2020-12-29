#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
# arr will always be 6x6
def hourglassSum(arr):
    sums = []
    for x in range(4):
        for y in range(4):
            row1 = arr[x][y] + arr[x][y+1] + arr[x][y+2]
            row2 = arr[x+1][y+1]
            row3 = arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
            sums.append((row1+row2+row3))
    return(max(sums))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()
