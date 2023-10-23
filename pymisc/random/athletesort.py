'''
Input:
5 3 <- n m
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1 <- k

k is indexed from 0 to m -1 and is used as Key

[[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]

Output:
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
'''


#!/bin/python3

import math
import os
import random
import re
import sys

def take_second(elem):
    return elem[k]

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    sort_arr = sorted(arr,key=lambda item: item[k])
    for i in sort_arr:
        print (*i) 

