from itertools import permutations
string1 = input()
inputlist = string1.split(" ")
characters = str(inputlist[0])
length = int(inputlist[1])
characterslist = [i for i in characters]
permutationlist = list(permutations(characterslist, length))
permutationlist.sort()
for i in permutationlist:
    print (*i,sep="")
