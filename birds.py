#!/bin/python3

import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    d = []
    for i in range(1,6):
        d.append(arr.count(i))
    count = max(d)
    bird = d.index(count)+1
    return bird

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
