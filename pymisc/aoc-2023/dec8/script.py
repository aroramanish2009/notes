import sys
import re
from itertools import combinations
from itertools import tee
from collections import OrderedDict
from collections import defaultdict

datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
    Lines = list(filter(None, Lines))

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

globallist = []
globaltotal = 0
def data_mass(LineList):
    global globallist
    global globaltotal
    LineListPairs = list(map(lambda x: (x[0], x[1]), pairwise(LineList)))
    mylist = []
    for LineListPair in LineListPairs:  
        mylist.append(LineListPair[1] - LineListPair[0])
    myset = set(mylist)
    if len(myset) == 1 and 0 in myset:
        globallist = reversed(globallist)
        count = 0 
        itemlastelement = 0
        for item in globallist:
            print (item)
            if count == 0:
                itemlastelement = item.pop(0)
                count += 1
            else:
                itemlastelement = item.pop(0) - itemlastelement
                count += 1
        print (itemlastelement)
        globallist = []
        globaltotal = itemlastelement
    else:
        globallist.append(mylist)
        data_mass(mylist)
     


'''
[[3, 3, 3, 3, 3]]
None
[[3, 3, 3, 3, 3], [2, 3, 4, 5, 6], [1, 1, 1, 1]]
None
[[3, 3, 3, 3, 3], [2, 3, 4, 5, 6], [1, 1, 1, 1], [3, 3, 5, 9, 15], [0, 2, 4, 6], [2, 2, 2]]
None
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
['0 3 6 9 12 15', '1 3 6 10 15 21', '10 13 16 21 30 45']
[0, 3, 6, 9, 12, 15]
[1, 3, 6, 10, 15, 21]
[10, 13, 16, 21, 30, 45]
[(0, 3), (3, 6), (6, 9), (9, 12), (12, 15)]
[(1, 3), (3, 6), (6, 10), (10, 15), (15, 21)]
[(10, 13), (13, 16), (16, 21), (21, 30), (30, 45)]
'''                    
        
def main():
    lasttotal = 0
    for Line in Lines:
        LineList = list(map(int,Line.split(' ')))
        #LineListPair = list(map(lambda x: (x[0], x[1]), pairwise(LineList)))
        data_mass(LineList)
        lastment = LineList.pop(0)
        lasttotal = lasttotal + (lastment - globaltotal)
    print (lasttotal)
    #print (Lines)
if __name__ == "__main__":
    main()
