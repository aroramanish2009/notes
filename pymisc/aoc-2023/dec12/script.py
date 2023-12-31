import sys
import re
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict

datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")

'''
====================================================================================================
.#.######
#...#....
#....####
#....####
#...#....
.#.######
##...#..#
###..#...
#.#.#####
..#.#....
.#.#..##.
.##.#....
.####.##.
#.##.####
#..######
0
====rotate====
0.####.###....##
1#....###..###..
2.......###.###.
3#....#....#.###
4##..##..##.##.#
5#.##.####....##
6#.##.#..#.#.###
7#.##.#..#.#.###
8#.##.##.#....##
====rotate====

#....#.
#....##
.####..
.####..
#....##
#.##.#.
.####.#
0
====rotate====
0##..##.
1..##..#
2..##.##
3..##.##
4..##..#
5##..##.
6.#..#.#
====rotate====
i 3
0##.###...#.##
1##.###...#.##
2###.#####..##
3##....#.##.##
4#....#.#.####
5.#....###....
6#....#...####
7.##.##.####..
8..#.##.###.#.
0

0##.#.##.#
1...#..#..
2.##...#..
3.##...#..
4.#.#..#..
5##.#.##.#
6.#...####
7..#.#..##
8...#...##
9.#....#.#
10.#....#.#
0

'''
def data_mass3(ListofList):
    for i in reversed(range(len(ListofList))):
        #print (ListofList)
        #print (ListofList[i],ListofList[i + 1],i,len(ListofList) - 1)
        if ListofList[i] == ListofList[i - 1]:
            if i == len(ListofList) - 1:
                return i
            elif i == 1:
                return 1
            else:
                aboveLine = i - 2
                belowLine = i + 1
                while 0 <= aboveLine and belowLine <= len(ListofList) - 1:
                    if ListofList[aboveLine] == ListofList[belowLine]:
                        if belowLine == len(ListofList) - 1:
                            return i
                        elif aboveLine == 0:
                            return i
                        aboveLine -= 1
                        belowLine += 1
                    else:
                        break
    return 0               
             
    
def data_mass2(ListofList):
    #print (ListofList)
    transListofList = []
    for item in list(map(list,zip(*ListofList))):
        transListofList.append(''.join(item))
    print ("====rotate====")
    print (*transListofList,sep="\n")
    print ("====rotate====")
    return data_mass3(transListofList) 
'''
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
['#.##..##.', '..#.##.#.', '##......#', '##......#', '..#.##.#.', '..##..##.', '#.#.##.#.']
diff2 [0, 3, 4, 5, 6]
0
str1,str2 = ListofList[aboveLine],ListofList[belowLine]
diff1 = [j for j in range(len(str1)) if str1[j] != str2[j]]
#....#.
#....##
.####..
.####..
#....##
#.##.#.
.####.#

.#...####.##..#
..#.###...#.##.
..#.###...#.##.
.#...####.##..#
.####..##.##..#
.####.#.###.##.
####..#.#######
#.......####..#
####.#.#.......
..#....##.#####
.##.##...##.###
..#.#.#.##.....
.....##.#..####
##..#.###..####
.##..#...######


.#...####.##..#
..#.###...#.##.
..#.###...#.##.
.#...####.##..#
.####..##.##..#
.####.#.###.##.
####..#.#######
#.......####..#
####.#.#.......
..#....##.#####
.##.##...##.###
..#.#.#.##.....
.....##.#..####
##..#.###..####
.##..#...######
['.#...####.##..#', '..#.###...#.##.']
['.#...####.##..#', '..#.###...#.##.']

'''
         
def part2(ListofList):
    oldline = data_mass3(ListofList)
    print (oldline)
    if oldline >= 0:
        count = 0
        for item in ListofList:
            for anitem in ListofList:
                str1,str2 = item,anitem
                diff1 = [j for j in range(len(str1)) if str1[j] != str2[j]]
                if len(diff1) == 1:
                    ListofList[count] = anitem
                    break
            count += 1
        print (ListofList)
        print (data_mass3(ListofList))
        return data_mass3(ListofList)
            


def main():
    total = 0 
    Lines.append("")
    ListofLists = []
    insidelist = []
    for Line in Lines:
        if Line != "":
            insidelist.append(Line)
        else:
            ListofLists.append(insidelist)
            insidelist = []
            
    #print (ListofLists)
    for ListofList in ListofLists:
        print (*ListofList,sep="\n")
        #print (data_mass(ListofList) * 100)
        #print (data_mass3(ListofList))
        #print (data_mass2(ListofList))
        #total += (data_mass3(ListofList) * 100)
        #total += data_mass2(ListofList)
        #print (data_mass3(ListofList))
        #print (data_mass2(ListofList))
        #print ("=" * 100)
        #print (part2(ListofList))
        total += (part2(ListofList) * 100)
    print (total)
if __name__ == "__main__":
    main()
