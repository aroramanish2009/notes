'''
.update() -> updates the set by adding elements from an iterable or another set
.intersection_update -> Update the set by keeping only the elements found in it and an iterable/another set
.difference_update -> Update the set by removing elements found in an iterable/another set.
.symmetric_difference_update() -> Update the set by only keeping the elements found in either set, but not in both.

Sample input
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66
'''

lenseta = int(input())
seta = set([int(i) for i in input().split()])
for i in range(int(input())):
    command = input().split()[0]
    setb = set()
    setb = set([ int(j) for j in input().split()])
    if command == "update":
        seta.update(setb)
    elif command == "intersection_update":
        seta.intersection_update(setb)
    elif command == "symmetric_difference_update":
        seta.symmetric_difference_update(setb)
    elif command == "difference_update":
        seta.difference_update(setb)

print (sum(seta))
