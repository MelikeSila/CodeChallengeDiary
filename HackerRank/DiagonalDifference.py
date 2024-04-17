#!/bin/python3
# DONE
# 11.04.2024

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
    
    j = -1
    line = 0
    left_sum, right_sum = 0, 0 
    for i in range(len(arr)):
        left_sum += arr[line][i]
        right_sum += arr[line][j]
        j -=1 
        line += 1
    
    print("left_sum:" +  str(left_sum)+ "right_sum:" + str(right_sum))
    return abs(left_sum - right_sum)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
