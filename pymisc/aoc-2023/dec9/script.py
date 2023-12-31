import sys
import re
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict

datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
    Lines = list(filter(None, Lines))

def data_mass(mylist):
    pass
def data_mass2(mylist):
    pass

def neighbors(grid, p):
    result = []
    x0, y0 = p
    for x1, y1 in [(x0 - 1, y0), (x0 + 1, y0), (x0, y0 - 1), (x0, y0 + 1)]:
        if 0 <= x1 < len(grid[0]) and 0 <= y1 < len(grid):
            result.append((x1, y1))
    return result                    

'''
[['.', '.', 'F', '7', '.'], ['.', 'F', 'J', '|', '.'], ['S', 'J', '.', 'L', '7'], ['|', 'F', '-', '-', 'J'], ['L', 'J', '.', '.', '.']]
5 5
[(1, 1), (3, 1), (2, 0), (2, 2)]
'''

        
def main():
    grid = [[i for i in line] for line in Lines]
    print (grid)
    gridrows = len(Lines)
    gridcol = set([len(line) for line in Lines]).pop()
    count = 0
    for item in grid:
        if "S" in item:
            start_x = count
            start_y = item.index("S")
        count += 1
    print (start_x,start_y)
             
    
if __name__ == "__main__":
    main()
