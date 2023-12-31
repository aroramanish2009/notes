import sys
import re
from itertools import combinations
from collections import OrderedDict
from collections import defaultdict

datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")
    Lines = list(filter(None, Lines))

def_dict = defaultdict(list)
count = 0 
for i in Lines:
    if re.search('seeds:',i):
        seedsstr = i.split(':')[1]
        seedslist = seedsstr.split(' ')
        seedslist = list(filter(None,seedslist))
    elif re.search(':',i):
        key = i.split(' ')[0]
        def_dict[key]
    elif re.search('^\d.*', i):
        def_dict[key].append(i)
    count += 1
#print (seedslist)
#print (def_dict)

'''
['79', '14', '55', '13']
defaultdict(<class 'list'>, {'seed-to-soil': ['50 98 2', '52 50 48'], 'soil-to-fertilizer': ['0 15 37', '37 52 2', '39 0 15'], 'fertilizer-to-water': ['49 53 8', '0 11 42', '42 0 7', '57 7 4'], 'water-to-light': ['88 18 7', '18 25 70'], 'light-to-temperature': ['45 77 23', '81 45 19', '68 64 13'], 'temperature-to-humidity': ['0 69 1', '1 0 69'], 'humidity-to-location': ['60 56 37', '56 93 4']})
81 53 60 49 56
81 11 52 0 41
81 0 6 42 48
81 7 10 57 60
81
53 53 60 49 56
53 11 52 0 41
53 0 6 42 48
53 7 10 57 60
53
57 53 60 49 56
57 11 52 0 41
57 0 6 42 48
57 7 10 57 60
57
52 53 60 49 56
52 11 52 0 41
52 0 6 42 48
52 7 10 57 60
52
'''
def data_mass1(seedslist,def_dict):
    locations = []
    for seed in seedslist:
        for item in def_dict['seed-to-soil']:
            dest_min = int(item.split(' ')[0])
            dest_max = int(item.split(' ')[0]) + int(item.split(' ')[2]) - 1
            src_min = int(item.split(' ')[1])
            src_max = int(item.split(' ')[1]) + int(item.split(' ')[2]) - 1
            if int(seed) > src_min and int(seed) < src_max:
                soil = dest_min + (int(seed) - src_min)
                break
            elif int(seed) == src_min:
                soil = dest_min
                break
            elif int(seed) == src_max:
                soil = dest_max
                break
            else:
                loc = seed
                continue
        for item in def_dict['soil-to-fertilizer']:
            dest_min = int(item.split(' ')[0])
            dest_max = int(item.split(' ')[0]) + int(item.split(' ')[2]) - 1
            src_min = int(item.split(' ')[1])
            src_max = int(item.split(' ')[1]) + int(item.split(' ')[2]) - 1
            if int(soil) > src_min and int(soil) < src_max:
                fert = dest_min + (int(soil) - src_min)
                break
            elif int(soil) == src_min:
                fert = dest_min
                break
            elif int(soil) == src_max:
                fert = dest_max
                break
            else:
                fert = soil
        for item in def_dict['fertilizer-to-water']:
            dest_min = int(item.split(' ')[0])
            dest_max = int(item.split(' ')[0]) + int(item.split(' ')[2]) - 1
            src_min = int(item.split(' ')[1])
            src_max = int(item.split(' ')[1]) + int(item.split(' ')[2]) - 1
            if int(fert) > src_min and int(fert) < src_max:
                wat = dest_min + (int(fert) - src_min)
                break
            elif int(fert) == src_min:
                wat = dest_min
                break
            elif int(fert) == src_max:
                wat = dest_max
                break
            else:
                wat = fert
        for item in def_dict['water-to-light']:
            dest_min = int(item.split(' ')[0])
            dest_max = int(item.split(' ')[0]) + int(item.split(' ')[2]) - 1
            src_min = int(item.split(' ')[1])
            src_max = int(item.split(' ')[1]) + int(item.split(' ')[2]) - 1
            if int(wat) > src_min and int(wat) < src_max:
                lgt = dest_min + (int(wat) - src_min)
                break
            elif int(wat) == src_min:
                lgt = dest_min
                break
            elif int(wat) == src_max:
                lgt = dest_max
                break
            else:
                lgt = wat
        for item in def_dict['light-to-temperature']:
            dest_min = int(item.split(' ')[0])
            dest_max = int(item.split(' ')[0]) + int(item.split(' ')[2]) - 1
            src_min = int(item.split(' ')[1])
            src_max = int(item.split(' ')[1]) + int(item.split(' ')[2]) - 1
            if int(lgt) > src_min and int(lgt) < src_max:
                tmp = dest_min + (int(lgt) - src_min)
                break
            elif int(lgt) == src_min:
                tmp = dest_min
                break
            elif int(lgt) == src_max:
                tmp = dest_max
                break
            else:
                tmp = lgt
        for item in def_dict['temperature-to-humidity']:
            dest_min = int(item.split(' ')[0])
            dest_max = int(item.split(' ')[0]) + int(item.split(' ')[2]) - 1
            src_min = int(item.split(' ')[1])
            src_max = int(item.split(' ')[1]) + int(item.split(' ')[2]) - 1
            if int(tmp) > src_min and int(tmp) < src_max:
                hum = dest_min + (int(tmp) - src_min)
                break
            elif int(tmp) == src_min:
                hum = dest_min
                break
            elif int(tmp) == src_max:
                hum = dest_max
                break
            else:
                hum = tmp
        for item in def_dict['humidity-to-location']:
            dest_min = int(item.split(' ')[0])
            dest_max = int(item.split(' ')[0]) + int(item.split(' ')[2]) - 1
            src_min = int(item.split(' ')[1])
            src_max = int(item.split(' ')[1]) + int(item.split(' ')[2]) - 1
            if int(hum) > src_min and int(hum) < src_max:
                loc = dest_min + (int(hum) - src_min)
                break
            elif int(hum) == src_min:
                loc = dest_min
                break
            elif int(hum) == src_max:
                loc = dest_max
                break
            else:
                loc = hum
        locations.append(loc)
    return (sorted(locations)[0])

'''
['79', '14', '55', '13']
defaultdict(<class 'list'>, {'seed-to-soil': ['50 98 2', '52 50 48'], 'soil-to-fertilizer': ['0 15 37', '37 52 2', '39 0 15'], 'fertilizer-to-water': ['49 53 8', '0 11 42', '42 0 7', '57 7 4'], 'water-to-light': ['88 18 7', '18 25 70'], 'light-to-temperature': ['45 77 23', '81 45 19', '68 64 13'], 'temperature-to-humidity': ['0 69 1', '1 0 69'], 'humidity-to-location': ['60 56 37', '56 93 4']})
[(79, 92), (55, 67)]
seed-to-soil
50 51 98 99 -48
52 99 50 97 2
81 94 2
soil-to-fertilizer
0 36 15 51 -15
37 38 52 53 -15
39 53 0 14 39
fertilizer-to-water
49 56 53 60 -4
0 41 11 52 -11
42 48 0 6 42
57 60 7 10 50
water-to-light
88 94 18 24 70
18 87 25 94 -7
74 87 -7
light-to-temperature
45 67 77 99 -32
42 55 -32
81 99 45 63 36
78 91 36
68 80 64 76 4
temperature-to-humidity
0 0 69 69 -69
1 69 0 68 1
humidity-to-location
60 96 56 92 4
82 95 4
56 59 93 96 -37
45 58 -37
45 58

'''
        
def data_mass2(trueseedslist,def_dict):
    locations = []
    for seedtup in trueseedslist:
        seedtup_min = seedtup[0]
        seedtup_max = seedtup[1]
        for k,v in def_dict.items():
            print (k)
            for item in v:
                dest_min = int(item.split(' ')[0])
                dest_max = int(item.split(' ')[0]) + int(item.split(' ')[2]) - 1
                src_min = int(item.split(' ')[1])
                src_max = int(item.split(' ')[1]) + int(item.split(' ')[2]) - 1
                offset = dest_min - src_min
                print (dest_min,dest_max,src_min,src_max,offset)
                #79 92
                #50 51 98 99 -48
                #52 99 50 97 2
                if seedtup_max < src_min or seedtup_min > src_max:
                    loc_min = seedtup_min
                    loc_max = seedtup_max
                elif seedtup_min >= src_min and seedtup_max <= src_max:
                    seedtup_min = seedtup_min + offset
                    seedtup_max = seedtup_max + offset
                elif seedtup_min >= src_min and seedtup_max > src_max:
                    seedtup_min = seedtup_min + offset
                    locations.append((src_max + 1,seedtup_max))
                    seedtup_max = src_max + offset
                elif seedtup_min < src_min and seedtup_max <= src_max:
                    #print (seedtup_min,src_min,seedtup_max,src_max,"HERE")
                    #74 77 87 99 HERE
                    #print (seedtup_min,src_min - seedtup_min)
                    locations.append((seedtup_min,src_min - 1))
                    seedtup_min = src_min + offset
                    seedtup_max = seedtup_max + offset
                elif seedtup_min < src_min and seedtup_max > src_max:
                    locations.append((src_max + 1,seedtup_max))
                    locations.append((seedtup_min,src_min - 1))
                    seedtup_min = src_min + offset
                    seedtup_max = src_max + offset
                print (seedtup_min,seedtup_max,offset)
                print (locations)
        loc_min = seedtup_min
        loc_max = seedtup_max
        if loc_min:
            locations.append((loc_min,loc_max))
    print (locations)
'''
79 92
seed-to-soil
50 98 2
52 50 48
soil-to-fertilizer
0 15 37
37 52 2
39 0 15
fertilizer-to-water
49 53 8
0 11 42
42 0 7
57 7 4
water-to-light
88 18 7
18 25 70
light-to-temperature
45 77 23
81 45 19
68 64 13
temperature-to-humidity
0 69 1
1 0 69
humidity-to-location
60 56 37
56 93 4
55 67
'''
def data_mass3(trueseedslist,def_dict):
    locations = []
    for seedtup in trueseedslist:
        seedtup_min = seedtup[0]
        seedtup_max = seedtup[1]
        print (seedtup_min,seedtup_max)
        for k,v in def_dict.items():
            print (k)
            print (len(v))
            for i in range(len(v)):
                src_min = int(v[i].split(' ')[1])
                dest_min = int(v[i].split(' ')[0])
                offset = int(v[i].split(' ')[2])
                #seedtup_max < src_min or seedtup_min > src_max
                if seedtup_min > (src_min + offset - 1) or seedtup_max < src_min:
                    mapped_min = seedtup_min
                    mapped_max = seedtup_max
                #seedtup_min >= src_min and seedtup_max <= src_max:
                elif seedtup_min >= src_min and seedtup_max <= (src_min + offset - 1):
                    mapped_min = seedtup_min + offset
                    mapped_max = seedtup_max + offset
                elif      
                 

def main():
    trueseedslist = []
    finallist = []
    anotherseedslist = []
    for i in range(0,len(seedslist) - 1, 2):
        start_seednum = int(seedslist[i])
        end_seednum = int(seedslist[i]) + int(seedslist[i + 1]) - 1
        trueseedslist.append((start_seednum,end_seednum))
    #print (trueseedslist)
    #print (data_mass1(anotherseedslist,def_dict))
    #data_mass2(trueseedslist,def_dict)
    data_mass3(trueseedslist,def_dict)

if __name__ == "__main__":
    main()
