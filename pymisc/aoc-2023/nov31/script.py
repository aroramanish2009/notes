import sys
import re
datafile = sys.argv[1]

with open(datafile, 'r') as sample_file:
    Lines=sample_file.read().strip().split("\n")

'''
['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''


def data_print(datalist):
    sumall = 0
    for i in datalist:
        sumall = sumall + int(re.sub("[^0-9]", "", i)[0] + re.sub("[^0-9]", "", i)[-1])
        print (re.sub("[^0-9]", "", i)[0])
        print (re.sub("[^0-9]", "", i)[-1])
        #re.sub("[^0-9]", "", i)[-1]
    print (sumall)


def data_p(datalist):
    sumall = 0
    replacements = [("one", "o1e"), ("two", "tw2o"),("three", "th3ee"), ("four", "fo4r"),("five", "fi5e"), ("six", "s6x"),("seven", "se7en"), ("eight", "ei8ght"),("nine", "n9ne")]
    for i in datalist:
        for pat,repl in replacements:
            i = re.sub(pat, repl, i)
        sumall = sumall + int(re.sub("[^0-9]", "", i)[0] + re.sub("[^0-9]", "", i)[-1])
    print (sumall)

        
def main():
    data_p(Lines)
    

if __name__ == "__main__":
    main()
