from itertools import combinations
string1 = input()
inputlist = string1.split(" ")
characters = str(inputlist[0])
characterlist = [ i for i in characters]
characterlist.sort()
length = int(inputlist[1])
for i in range(1, length + 1):
    mylist = list(combinations(characterlist,i))
    print (mylist)
    for j in mylist:
        print (*j,sep="")
