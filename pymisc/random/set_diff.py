lenset1 = int(input())
set1 = set(map(int, input().split(" ")))
lenset2 = int(input())
set2 = set(map(int, input().split(" ")))
symmdiffset = set()
symmdiffset.update(set1.difference(set2))
symmdiffset.update(set2.difference(set1))
for i in sorted(symmdiffset):
    print (i)
