#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import timedelta,datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z" 
    dt1 = datetime.strptime(t1, format_string)
    dt2 = datetime.strptime(t2, format_string) 
    diff = abs(dt1 - dt2)
    return str(int(diff.total_seconds()))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
