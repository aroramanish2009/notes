import sys
import re
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict

datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
    Lines = list(filter(None, Lines))

def data_mass(timelist,distlist):
    print (timelist,distlist)
    product = 1
    for i in range(len(timelist)):
        count = 0 
        for ii in range(1,timelist[i] + 1):
            if (timelist[i] - ii) * ii > distlist[i]:
                count += 1
        product = product * count
    print (product)
             
def data_mass2(mylist):
    pass
                    
        
def main():
    for i in Lines:
        if re.search('Time', i):
            timestr = i.split(':')[1].strip()
            timestr = re.sub(' +', '',timestr)
            timelist = list(map(int,timestr.split(' ')))
        else:
            diststr = i.split(':')[1].strip()
            diststr = re.sub(' +', '',diststr)
            distlist = list(map(int,diststr.split(' ')))
    data_mass(timelist,distlist)
    data_mass2(Lines)

if __name__ == "__main__":
    main()
