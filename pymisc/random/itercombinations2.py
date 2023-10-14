from itertools import combinations
N = int(input())
mystr = input()
K = int(input())
mycombs = combinations(''.join(mystr.split(" ")), K)
totalcombs = 0
itemcombs = 0
for item in mycombs:
    totalcombs += 1
    if "a" in item:
        itemcombs += 1
print (round (itemcombs / totalcombs, 4))
