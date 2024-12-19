import sys
from itertools import combinations
from more_itertools import pairwise
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
  safe = 0
  for line in Lines:
    linelist = [int(x) for x in line.split(" ")]
    #print (linelist)
    #print ("Rsorted",sorted(linelist,reverse=True))
    #print ("sorted",sorted(linelist))
    if linelist == sorted(linelist,reverse=True):
      level = []
      for x,y in pairwise(linelist):
        level.append(int(x) - int(y))
      if max(level) < 4 and min(level) != 0:
        safe += 1
    elif linelist == sorted(linelist):
      level = []
      for x,y in pairwise(linelist):
        level.append(int(y) - int(x))
      if max(level) < 4 and min(level) != 0:
        safe += 1
  print (safe)

def testtole(linelist):
  for i in range(len(linelist)):
    newlinelist = linelist.copy()
    newlinelist.pop(i)
    print ("intest",newlinelist)
    if newlinelist == sorted(newlinelist,reverse=True) or newlinelist == sorted(newlinelist):
      tlevel = []
      for x,y in pairwise(newlinelist):
        tlevel.append(abs(int(x) - int(y)))
      if max(tlevel) < 4 and min(tlevel) != 0:
        print ("intest",tlevel)
        return (True)
  return (False)

def part2(datafile):
  with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
  safe = 0
  for line in Lines:
    linelist = [int(x) for x in line.split(" ")]
    if linelist == sorted(linelist,reverse=True) or linelist == sorted(linelist):
      level = []
      for x,y in pairwise(linelist):
        level.append(abs(int(x) - int(y)))
      if max(level) < 4 and min(level) != 0:
        safe += 1
      else:
        print ("linelist",linelist)
        if testtole(linelist):
          safe += 1
    else:
      if testtole(linelist):
        safe += 1
  print (safe)

        
def main():
  #part1(datafile)
  part2(datafile)

if __name__ == "__main__":
    main()
