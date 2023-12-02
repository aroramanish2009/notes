import sys
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict
datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")

'''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
['6 red, 1 blue, 3 green', ' 2 blue, 1 red, 2 green']
{'1': ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green'], '2': ['1 blue, 2 green', '3 green, 4 blue, 1 red', '1 green, 1 blue'], '3': ['8 green, 6 blue, 20 red', '5 blue, 4 red, 13 green'5 green, 1 red'], '4': ['1 green, 3 red, 6 blue', '3 green, 6 red', '3 green, 15 blue, 14 red'], '5': ['6 red, 1 blue, 3 green', '2 blue, 1 red, 2 green']}
==
{'1': [['3 blue, 4 red'], ['1 red, 2 green, 6 blue'], ['2 green']], '2': [['1 blue, 2 green'], ['3 green, 4 blue, 1 red'], ['1 green, 1 blue']], '3': [['8 green, 6 blue, 20 red'], ['5 blue, 4 red, 13 green'], ['5 green, 1 red']], '4': [['1 green, 3 red, 6 blue'], ['3 green, 6 red'], ['3 green, 15 blue, 14 red']], '5': [['6 red, 1 blue, 3 green'], ['2 blue, 1 red, 2 green']]}
{'blue': 6, 'red': 4, 'green': 2}
{'blue': 4, 'green': 3, 'red': 1}
{'green': 13, 'blue': 6, 'red': 20}
{'green': 3, 'red': 14, 'blue': 15}
{'red': 6, 'blue': 2, 'green': 3}

'''              
def data_mass(datalist):
    dataset = {}
    sumall = 0
    for item in datalist:
        gameid,gamesets = item.split(':')[0],item.split(':')[1].strip()
        dataset[gameid.split(' ')[1]] = [i.strip() for i in gamesets.split(';')]
    for k,v in dataset.items():
        invalid = False
        for i in v:
            eachcolor = i.split(',')
            for ii in eachcolor:
                ii = ii.strip()
                if ii.split(' ')[1] == "red" and int(ii.split(' ')[0]) > 12:
                    invalid = True
                elif ii.split(' ')[1] == "green" and int(ii.split(' ')[0]) > 13:
                    invalid = True
                elif ii.split(' ')[1] == "blue" and int(ii.split(' ')[0]) > 14:
                    invalid = True
        if invalid == False:
            sumall = sumall + int(k)
    print (sumall)

        
def main():
    data_mass(Lines)

if __name__ == "__main__":
    main()
