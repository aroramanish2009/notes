from collections import defaultdict

sizegr = str(input())
sizegra = int(sizegr.split(" ")[0])
sizegrb = int(sizegr.split(" ")[1])
dset = defaultdict(list)
for i in range(sizegra + sizegrb):
    if i < (sizegra):
        dset['A'].append(str(input()))
    else:
        dset['B'].append(str(input()))

def get_indices(element, lst):
    return [i for i, x in enumerate(lst) if x == element]
count = 0
for bitem in dset['B']:
    count += 1
    indexlist = []
    indexlist = get_indices(bitem, dset['A'])
    if indexlist:
        for i in indexlist:
            print (i + 1, end=" ")
    else:
        print ("-1", end=" ")
    if count < len(dset['B']):
        print ()


