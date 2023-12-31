import sys
import re
from itertools import combinations
from itertools import groupby
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
from functools import cmp_to_key

datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
    Lines = list(filter(None, Lines))
'''
233KT
555JT
677KK
JJKTT
AJQQQ
['2', '3', '3', 'K', 'T']
Counter({'3': 2, '2': 1, 'K': 1, 'T': 1})
dict_values([1, 2, 1, 1])
['5', '5', '5', 'J', 'T']
Counter({'5': 3, 'J': 1, 'T': 1})
dict_values([3, 1, 1])
['6', '7', '7', 'K', 'K']
Counter({'7': 2, 'K': 2, '6': 1})
dict_values([1, 2, 2])
['J', 'J', 'K', 'T', 'T']
Counter({'J': 2, 'T': 2, 'K': 1})
dict_values([2, 1, 2])
['A', 'J', 'Q', 'Q', 'Q']
Counter({'Q': 3, 'A': 1, 'J': 1})
dict_values([1, 1, 3])
defaultdict(<class 'list'>, {'onepair': [('233KT', 765)], 'threekind': [('555JT', 684), ('AJQQQ', 483)], 'twopair': [('677KK', 28), ('JJKTT', 220)]})
'''

def data_mass(mylist):
    total = 0
    def_dict = defaultdict(list)
    for i in mylist:
        myhand,bid = i.split(' ')[0],i.split(' ')[1]
        bid = int(bid)
        myhandsort = sorted(myhand)
        counts = Counter(myhandsort)
        values = counts.values()
        if len(counts) == 5:
            def_dict['highcard'].append((myhand,bid))
        elif len(counts) == 4:
            def_dict['onepair'].append((myhand,bid))
        elif len(counts) == 3 and 2 in values:
            def_dict['twopair'].append((myhand,bid))
        elif len(counts) == 3 and 3 in values:
            def_dict['threekind'].append((myhand,bid))
        elif len(counts) == 2 and 3 in values:
            def_dict['fullhouse'].append((myhand,bid))
        elif len(counts) == 2 and 4 in values:
            def_dict['fourkind'].append((myhand,bid))
        elif len(counts) == 1:
            def_dict['fivekind'].append((myhand,bid))
    max_rank = len(mylist)
    print (def_dict)
    for k,v in def_dict.items():
        print (v)
        v = sorted(v,key=lambda x: x[0],reverse=True)
        print (v)
    if def_dict['fivekind']:
        for j in def_dict['fivekind']:
            total = total + (max_rank * j[1])
            max_rank -= 1
    if def_dict['fourkind']:
        for j in def_dict['fourkind']:
            total = total + (max_rank * j[1])
            max_rank -= 1
    if def_dict['fullhouse']:
        for j in def_dict['fullhouse']:
            total = total + (max_rank * j[1])
            max_rank -= 1
    if def_dict['threekind']:
        for j in def_dict['threekind']:
            print ("==",j[0])
            total = total + (max_rank * j[1])
            print (max_rank,j[1])
            max_rank -= 1
    if def_dict['twopair']:
        for j in def_dict['twopair']:
            print ("==",j[0])
            total = total + (max_rank * j[1])
            print (max_rank,j[1])
            max_rank -= 1
    if def_dict['onepair']:
        for j in def_dict['onepair']:
            total = total + (max_rank * j[1])
            print (max_rank,j[1])
            max_rank -= 1
    if def_dict['highcard']:
        for j in def_dict['highcard']:
            total = total + (max_rank * j[1])
            max_rank -= 1
    print (def_dict)
    print (total)    

def data_mass2(mylist):
    pass
                    
        
def main():
    data_mass(Lines)
    #data_mass2(Lines)

if __name__ == "__main__":
    main()
