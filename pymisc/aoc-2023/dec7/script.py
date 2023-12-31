import sys
import re
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict
from math import lcm

datafile = sys.argv[1]
'''
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)

'''
with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
    Lines = list(filter(None, Lines))

def data_mass(mylist):
    print (mylist) 
def data_mass2(mylist):
    pass
                    
        
def main():
    count = 0
    def_dict = defaultdict(list)
    for i in Lines:
        if "=" in i:
            key = i.split("=")[0].strip()
            val = i.split("=")[1].strip()
            print (key,val)
            def_dict[key] = (val)
        else:
            mystr = i.strip()
    print (mystr)
    print (def_dict)
    nextstep = "AAA"
    while nextstep != "ZZZ":
        for turn in mystr:
            if turn == "L":
                nextstep = def_dict[nextstep][1:4]
                count += 1
            elif turn == "R":
                print (def_dict[nextstep][6:9])
                nextstep = def_dict[nextstep][6:9]
                count += 1
    print (count)

    def_dict = defaultdict(list)
    for i in Lines:
        if "=" in i:
            key,val = i.split("=")[0].strip(),i.split("=")[1].strip()
            def_dict[key] = (val)
        else:
            mystr = i.strip()
    mylist = list(mystr)
    print (mylist)
    totalsteps = []
    for mynode in def_dict.keys():
        if mynode.endswith("A"):
            count2 = 0
            while not bool(mynode.endswith("Z")):
                for turn in mylist:
                    if turn == "L":
                        mynode = def_dict[mynode][1:4]
                        count2 += 1
                    elif turn == "R":
                        mynode = def_dict[mynode][6:9]
                        count2 += 1
                    if mynode.endswith("Z") is True:
                        break
            if count2 != 0:
                totalsteps.append(count2)
    print (totalsteps)
    print (*totalsteps)
    print (lcm(*totalsteps))
                        

if __name__ == "__main__":
    main()
