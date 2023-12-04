import sys
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict

datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")


def data_mass(datalist):
    print (datalist)

def data_mass2(datalist):
    print ("Num2")
                
        
        
def main():
    data_mass(Lines)
    data_mass2(Lines)

if __name__ == "__main__":
    main()
