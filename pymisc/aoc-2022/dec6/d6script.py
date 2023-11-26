import sys
from collections import Counter
datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")

def data_print(datalist):
    mystr = datalist[0]
    for i in range(0,len(mystr)):
        if len(mystr[i:i+14]) == len(Counter(mystr[i:i+14])):
            return (i + 14)
        
def main():
    print (data_print(Lines))

if __name__ == "__main__":
    main()
