#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(ar):
    p=0
    d=set(ar)
    for i in d:
        p+=ar.count(i)//2
    return p
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
