
import sys
from collections import defaultdict
inline = sys.argv[1] if len(sys.argv)>1 else 'crap.txt'
data = open(inline).read().strip()
lines = [x for x in data.split('\n')]

M = []
OP = []
DIV = []
TRUE = []
FALSE = []
for monkey in data.split('\n\n'):
    id_, items, op, test, true, false = monkey.split('\n')
    M.append([int(i) for i in items.split(':')[1].split(',')])
    words = op.split()
    op = ''.join(words[-3:])
    OP.append(lambda old,op=op:eval(op))
    DIV.append(int(test.split()[-1]))
    TRUE.append(int(true.split()[-1]))
    FALSE.append(int(false.split()[-1]))
print(M)

C = [0 for _ in range(len(M))]
for _ in range(20):
    for i in range(len(M)):
        for item in M[i]:
            C[i] += 1
            item = OP[i](item)
            item = (item // 3)
            if item % DIV[i] == 0:
                M[TRUE[i]].append(item)
            else:
                M[FALSE[i]].append(item)
        M[i] = []

print (sorted(C))
print (sorted(C)[-1] * (sorted(C)[-2]))
