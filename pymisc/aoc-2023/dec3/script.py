import sys
import re
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict

datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
'''
Card 1: 41 48 83 86 17   83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61   61 30 68 82 17 32 24 19
'''

def data_mass(datalist):
    sumall = 0 
    for i in datalist:
        winningnumstring,yournumstring = i.split('|')
        winningnumstring = winningnumstring.split(':')[1]
        winningnumstring = winningnumstring.strip()
        yournumstring = yournumstring.strip()
        yournumlist = yournumstring.split(' ')
        winningnumlist = winningnumstring.split(' ')
        yournumlist = list(filter(None, yournumlist))
        winningnumlist = list(filter(None,winningnumlist))
        yournumset = set(yournumlist)
        winningnum = set(winningnumlist)
        matches = len(yournumset.intersection(winningnum))
        if matches == 1:
            sumall += 1
        elif matches > 1:
            count = sum([2**i for i in range(matches - 1)])
            sumall = sumall + count + 1
            
    print (sumall)
'''
defaultdict(<class 'list'>, {1: [1], 2: [1], 3: [1], 4: [1], 5: [1]})
defaultdict(<class 'list'>, {1: [1], 2: [1, 1], 3: [1, 1, 1], 4: [1, 1, 1], 5: [1]})
defaultdict(<class 'list'>, {1: [1], 2: [1, 1], 3: [1, 1, 1, 1], 4: [1, 1, 1, 1, 1, 1, 1], 5: [1, 1, 1, 1, 1]})
defaultdict(<class 'list'>, {1: [1], 2: [1, 1], 3: [1, 1, 1, 1], 4: [1, 1, 1, 1, 1, 1, 1, 1], 5: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]})
defaultdict(<class 'list'>, {1: [1], 2: [1, 1], 3: [1, 1, 1, 1], 4: [1, 1, 1, 1, 1, 1, 1, 1], 5: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]})
defaultdict(<class 'list'>, {1: [1], 2: [1, 1], 3: [1, 1, 1, 1], 4: [1, 1, 1, 1, 1, 1, 1, 1], 5: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 6: [1]})

'''
def data_mass2(datalist):
    total = 0
    def_dict = defaultdict(list)
    for i in datalist:
        winningnumstring,yournumstring = i.split('|')
        winningcardstring,winningnumstring = winningnumstring.split(':')
        winningcardstring = re.sub(' +', ' ',winningcardstring)
        winningcardstring = winningcardstring.split(' ')[1]
        winningcardstring = winningcardstring.strip()
        def_dict[int(winningcardstring)].append(1)
        winningnumstring = winningnumstring.strip()
        yournumstring = yournumstring.strip()
        yournumlist = yournumstring.split(' ')
        winningnumlist = winningnumstring.split(' ')
        yournumlist = list(filter(None, yournumlist))
        winningnumlist = list(filter(None,winningnumlist))
        yournumset = set(yournumlist)
        winningnum = set(winningnumlist)
        matches = len(yournumset.intersection(winningnum))
        if matches > 0:
            start = int(winningcardstring) + 1
            end = int(winningcardstring) + matches
            for ii in range(start,end + 1):
                if len(def_dict[int(winningcardstring)]) > 1:
                    for i in range(len(def_dict[int(winningcardstring)])):
                        def_dict[ii].append(1)
                else:
                    def_dict[ii].append(1)
    total = 0
    for k,v in def_dict.items():
        total = total + len(v)
    print (total)
        
                
        
        
def main():
    #data_mass(Lines)
    data_mass2(Lines)

if __name__ == "__main__":
    main()
