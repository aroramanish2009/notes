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
                    
        
def main():
    print (Lines)
if __name__ == "__main__":
    main()
