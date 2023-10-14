'''
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
[['5', '4'], ['7', '8', '9'], ['5', '7', '8', '9', '10']]

'''

from itertools import product

KM = input()
K = int(KM.split(" ")[0])
M = int(KM.split(" ")[1])
available_list = []

for i in range(K):
    mystr = str(input())[1:].strip()
    available_list.append(list(map(int,mystr.split(' '))))

finalSlist = []
for _ in product(*available_list):
    finalSlist.append(sum(list(map(lambda x: x *x, _)))%M)

print (max(finalSlist))
