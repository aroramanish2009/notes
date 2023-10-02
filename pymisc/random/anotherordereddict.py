'''
Input Format

The first line contains the integer,
.
The next

lines each contain a word.

Output Format

Output
lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
Input: 
4
bcdef
abcdefg
bcde
bcdef

output:
3
2 1 1
'''
from collections import OrderedDict
myordict = OrderedDict()
for i in range(int(input())):
    key = str(input())
    value = 1
    if key not in myordict:
        myordict[key] = value
    else:
        value = value + myordict[key]
        myordict[key] = value
print (len(myordict))
for k,v in myordict.items():
    print (v,end=" ")
