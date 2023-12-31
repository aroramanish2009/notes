import sys
import re
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict
from functools import cache

datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
    Lines = list(filter(None, Lines))

@cache
def data_mass(document,numbers):
    print (document,numbers)
    if document == "":
        if numbers == ():
            return 1
        else:
            return 0
    if numbers == ():
        if "#" in document:
            return 0
        else:
            return 1

    result = 0 
    if document[0] in ".?":
        result += data_mass(document[1:],numbers)
    if document[0] in "#?":
        if numbers[0] <= len(document) and "." not in document[:numbers[0]] and (numbers[0] == len(document) or document[numbers[0]] != "#"):
            result += data_mass(document[numbers[0] + 1:],numbers[1:])
    return result 

def data_mass2(mylist):
    pass
'''
['???.### 1,1,3', '.??..??...?##. 1,1,3', '?#?#?#?#?#?#?#? 1,3,1,6', '????.#...#... 4,1,1', '????.######..#####. 1,6,5', '?###???????? 3,2,1']
???.### (1, 1, 3)
??.### (1, 1, 3)
?.### (1, 1, 3)
.### (1, 1, 3)
### (1, 1, 3)
### (1, 3)
.### (1, 3)
### (1, 3)
?.### (1, 3)
.### (1, 3)
### (1, 3)
### (3,)
 ()
===========
.??..??...?##. (1, 1, 3)
??..??...?##. (1, 1, 3)
?..??...?##. (1, 1, 3)
..??...?##. (1, 1, 3)
.??...?##. (1, 1, 3)
??...?##. (1, 1, 3)
?...?##. (1, 1, 3)
...?##. (1, 1, 3)
..?##. (1, 1, 3)
.?##. (1, 1, 3)
?##. (1, 1, 3)
##. (1, 1, 3)
..?##. (1, 3)
.?##. (1, 3)
?##. (1, 3)
##. (1, 3)
...?##. (1, 3)
..?##. (1, 3)
.?##. (1, 3)
?##. (1, 3)
##. (1, 3)
.??...?##. (1, 3)
??...?##. (1, 3)
?...?##. (1, 3)
...?##. (1, 3)
..?##. (1, 3)
.?##. (1, 3)
?##. (1, 3)
##. (1, 3)
..?##. (3,)
.?##. (3,)
?##. (3,)
##. (3,)
 ()
...?##. (3,)
..?##. (3,)
.?##. (3,)
?##. (3,)
##. (3,)
 ()
..??...?##. (1, 3)
.??...?##. (1, 3)
??...?##. (1, 3)
?...?##. (1, 3)
...?##. (1, 3)
..?##. (1, 3)
.?##. (1, 3)
?##. (1, 3)
##. (1, 3)
..?##. (3,)
.?##. (3,)
?##. (3,)
##. (3,)
 ()
...?##. (3,)
..?##. (3,)
.?##. (3,)
?##. (3,)
##. (3,)
 ()
'''                    
        
def main():
    total = 0 
    for Line in Lines:
        document,numbers = Line.split(' ')[0],Line.split(' ')[1]
        numbers = tuple(map(int,numbers.split(",")))
        total = total + data_mass(document,numbers)
    print (total)
    totalpart2 = 0
    for Line in Lines:
        document,numbers = Line.split(' ')[0],Line.split(' ')[1]
        numbers = tuple(map(int,numbers.split(",")))
        numbers = numbers * 5
        document = (document + "?" )* 5
        print (document[:-1],numbers)
        totalpart2 = totalpart2 + data_mass(document[:-1],numbers)
    print (totalpart2)

if __name__ == "__main__":
    main()
