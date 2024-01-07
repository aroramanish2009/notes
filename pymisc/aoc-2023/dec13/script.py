import sys
import re
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict

datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
    Lines = list(filter(None, Lines))
    NewLines = Lines[0].split(',')
'''
['rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7']
['rn=1', 'cm-', 'qp=3', 'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5', 'pc-', 'pc=6', 'ot=7']
Part1: 1320
defaultdict(<class 'list'>, {'Box 0': ['rn 1', 'cm 2'], 'Box 1': [], 'Box 3': ['ab 5', 'pc 6', 'ot 7']})
Part1: 1320
Box 0 ['rn 1', 'cm 2']
Box 1 []
Box 3 ['ot 7', 'ab 5', 'pc 6']
'''


def data_mass(item):
    startval = 0
    for i in item:
        startval = ((startval + ord(i)) * 17) % 256
    return startval
        
def data_mass2(item):
    if "=" in item:
        newitem = item.split("=")[0]
    elif "-" in item:
        newitem = item.split("-")[0]
    box = 0
    for i in newitem:
        box = ((box + ord(i)) * 17) % 256
    return box
                    
        
def main():
    total = 0
    for item in NewLines:
        total = total + data_mass(item)
    print ("Part1:",total)
    mydict = defaultdict(list)
    for item in NewLines:
        box = data_mass2(item)
        key = "Box " + str(box)
        if "=" in item:
            boxlist = mydict.get(key)
            myfact = False
            if boxlist:
                for iii in range(len(boxlist)):
                    if boxlist[iii].split(" ")[0] == item.split("=")[0]:
                        mydict[key][iii] = item.replace("=", " ")
                        myfact = True
                if myfact == False:
                    mydict[key].append(item.replace("=", " "))
            else:
                mydict[key].append(item.replace("=", " "))
        elif "-" in item:
            boxlist = mydict.get(key)
            if boxlist:
                for kk in range(len(boxlist)):
                    if boxlist[kk].split(" ")[0] == item.split("-")[0]:
                        del mydict[key][kk]
                        break
    totalpart2 = 0
    for k,v in mydict.items():
        boxval = int(k.split(' ')[1]) + 1
        count = 1
        for jj in v:
            totalpart2 = totalpart2 + (boxval * count * int(jj.split(' ')[1]))
            count += 1
    print ("part2:",totalpart2)
if __name__ == "__main__":
    main()
