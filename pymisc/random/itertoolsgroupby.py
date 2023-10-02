'''
Input:
aabbbbbbsssssaaaaa
output:
a 2
b 6
s 5
a 5

WITH LAMBDA
A 2
B 6
S 5
A 5
'''
from itertools import groupby
mystr = str(input())
for k,v in groupby(mystr,lambda x: x.upper()):
    print (k, len(list(v)))
