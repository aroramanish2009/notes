'''
 re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda). 
import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")

Output:
1 4 9 16 25 36 49 64 81
'''
import re
mylist = []
for i in range(int(input())):
    mystr = input()
    mystr = re.sub("(?<=\s)(\&\&)(?=\s)", "and",mystr)
    mystr = re.sub("(?<=\s)(\|\|)(?=\s)", "or",mystr)
    mylist.append(mystr)
print (*mylist,sep="\n")
