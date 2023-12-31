import sys
import re
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict
from collections import deque

datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
    Lines = list(filter(None, Lines))

def finddist(loc1,loc2):
    loc1a,loc1b = loc1
    loc2a,loc2b = loc2
    loc1a,loc2a = min(loc1a,loc2a), max(loc1a,loc2a)
    loc1b,loc2b = min(loc1b,loc2b), max(loc1b,loc2b)
    senddata = 0
    for i in range(loc1a, loc2a):
        senddata += 1
    for j in range(loc1b, loc2b):
        senddata += 1
    return (senddata)
        
def finddist2(loc1,loc2,dotallrow,dotallcol):
    loc1a,loc1b = loc1
    loc2a,loc2b = loc2
    loc1a,loc2a = min(loc1a,loc2a), max(loc1a,loc2a)
    loc1b,loc2b = min(loc1b,loc2b), max(loc1b,loc2b)
    senddata = 0
    for i in range(loc1a, loc2a):
        senddata += 1
        if dotallrow[i]:
            senddata += 10**6 - 1
    for j in range(loc1b, loc2b):
        senddata += 1
        if dotallcol[j]:
            senddata += 10**6 - 1
    return (senddata)
'''
(39python) root@ip-172-26-3-150:~/notes/pymisc/aoc-2023/dec10# python script.py sample.txt
['...#......', '.......#..', '#.........', '..........', '......#...', '.#........', '.........#', '..........', '.......#..', '#...#.....']
(39python) root@ip-172-26-3-150:~/notes/pymisc/aoc-2023/dec10#
[3, 7, 0, 6, 1, 9, 7, 0, 4]
[['.', '.', '.', '.', 1, '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', 2, '.', '.', '.'], [3, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', 4, '.', '.', '.', '.'], ['.', 5, '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 6], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.', 7, '.', '.', '.'], [8, '.', '.', '.', '.', 9, '.', '.', '.', '.', '.', '.', '.']]
[(0, 4), (1, 9), (2, 0), (3, 8), (4, 1), (5, 12), (6, 9), (7, 0), (8, 5)]
(0, 4) 0 4
(1, 9) 1 9
(0, 4) 0 4
(1, 9) 1 9
'''                    

def main():
    expandedLines = []
    galaxypos = []
    count = 0
    for Line in Lines:
        if '#' not in Line:
            expandedLines.append(Line)
            expandedLines.append(Line)
        else:
            for i in range(len(Line)):
                if Line[i] == "#" and i not in galaxypos:
                    galaxypos.append(i)
            expandedLines.append(Line)
        count += 1
    galaxypos = sorted(galaxypos)
    expandedLinesList = [list(i) for i in expandedLines]
    for item in expandedLinesList:
        for i in reversed(range(len(item))):
            if i not in galaxypos:
                item.insert(i,'.')
    galaxyloc = []
    for i in range(len(expandedLinesList)):
        for ii in range(len(expandedLinesList[i])):
            if expandedLinesList[i][ii] == '#':
                galaxyloc.append((i,ii))
    total = 0
    for ii in range(len(galaxyloc)):
        for jj in range(ii + 1,len(galaxyloc)):
            dist = finddist(galaxyloc[ii],galaxyloc[jj])
            total = total + dist 
    print (total)
    print (Lines)
    newgalaxyloc = []
    for i in range(len(Lines)):
        for ii in range(len(Lines[i])):
            if Lines[i][ii] == '#':
                newgalaxyloc.append((i,ii))
    print (newgalaxyloc)
    gridlen,gridwidth = len(Lines),len(Lines[0])
    print(gridlen,gridwidth)
    dotallrow = [all([Lines[i][j] == "." for j in range(gridwidth)]) for i in range(gridlen)]
    dotallcol = [all([Lines[i][j] == "." for i in range(gridlen)]) for j in range(gridwidth)]
    print (dotallcol,dotallcol)
    newtotal = 0
    for ii in range(len(newgalaxyloc)):
        for jj in range(ii + 1,len(newgalaxyloc)):
            dist = finddist2(newgalaxyloc[ii],newgalaxyloc[jj],dotallrow,dotallcol)
            newtotal = newtotal + dist
    print (newtotal)
if __name__ == "__main__":
    main()
