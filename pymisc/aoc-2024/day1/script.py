import sys
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict
datafile = sys.argv[1]

def readdata(datafile):
  with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
  list1 = []
  list2 = []
  for Line in Lines:
    #print (Line.split()[0])
    list1.append(Line.split()[0])
    list2.append(Line.split()[1])

  list1 = sorted(list1)
  list2 = sorted(list2)
  print (sum(list(map(lambda x,y: (abs(int(x)-int(y))),list1,list2))))

def part2(datafile):
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
  
  sscore = []
  for k,v in dict1.items():
    sscore.append((v * int(k)) * int(dict2.get(k) or 0))

  print (sum(sscore))
  

'''
3   4
4   3
2   5
1   3
3   9
3   3
{'3': 3, '4': 1, '2': 1, '1': 1}
{'4': 1, '3': 3, '5': 1, '9': 1}
'''

        
def main():
  #readdata(datafile)
  part2(datafile)

if __name__ == "__main__":
    main()
