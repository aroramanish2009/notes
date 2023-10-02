'''
Input:
szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni
Output:
o 12
m 11
n 11

Groupby Code:
from itertools import groupby

mystr = ''.join(sorted(input()))
mylist = []
for k,v in groupby(mystr):
    mylist.append((k, len(list(v))))
mylist = sorted(mylist,reverse=True,key=lambda x: x[1])
top3 = 1
for i in mylist:
    if top3 < 4:
        print (i[0],i[1])
        top3 += 1
    else:
        break
'''

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
[print(*elem) for elem in Counter(sorted(input())).most_common(3)]
