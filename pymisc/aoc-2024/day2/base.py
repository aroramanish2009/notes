import sys
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict
datafile = sys.argv[1]

'''
  with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
  list1 = []
  list2 = []
  for Line in Lines:
    #print (Line.split()[0])
    list1.append(Line.split()[0])
    list2.append(Line.split()[1])
  dict1 = {i:list1.count(i) for i in list1}
  dict2 = {j:list2.count(j) for j in list2}
'''

def part1(datafile):
  with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
  pass

def part2(datafile):
  with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
  pass 

        
def main():
  part1(datafile)
  part2(datafile)

if __name__ == "__main__":
    main()
