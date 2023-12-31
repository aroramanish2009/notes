import sys
import re
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict

datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
    Lines = list(filter(None, Lines))

def data_mass(commands):
    pass
def data_mass2(mylist):
    pass
'''
['R 6 (#70c710)', 'D 5 (#0dc571)', 'L 2 (#5713f0)', 'D 2 (#d2c081)', 'R 2 (#59c680)', 'D 2 (#411b91)', 'L 5 (#8ceee2)', 'U 2 (#caa173)', 'L 1 (#1b58a2)', 'U 2 (#caa171)', 'R 2 (#7807d2)', 'U 3 (#a77fa3)', 'L 2 (#015232)', 'U 2 (#7a21e3)']
'''                    
        
def main():
    print (Lines)
    commands = []
    for Line in Lines:
        direction,steps = Line.split(' ')[0],Line.split(' ')[1]
        commands.append((direction,steps))
   
if __name__ == "__main__":
    main()
